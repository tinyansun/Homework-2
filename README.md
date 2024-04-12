# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution
step 1:
amountIn: 5 tokenB
amountOut: 5.655321988655322 tokenA

step 2:
amountIn: 5.655321988655322 tokenA
amountOut: 2.37213893638309 tokenC

step 3:
amountIn: 2.37213893638309 tokenC
amountOut: 1.5301371369636172 tokenE

step 4:
amountIn: 1.5301371369636172 tokenE
amountOut: 3.450741448619709 tokenD

step 5:
amountIn: 3.450741448619709 tokenD
amountOut: 6.68452557957259 tokenC

step 6:
amountIn: 6.68452557957259 tokenC
amountOut: 22.497221806974142 tokenB

final reward: 22.497221806974142 tokenB

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Solution
Slippage in the context of Automated Market Makers (AMMs) like Uniswap V2 refers to the difference between the expected price of a trade and the actual executed price due to market fluctuations or changes in liquidity between the time of the trade's initiation and its settlement.
Uniswap V2 addresses slippage through its design and automated pricing mechanism, which relies on the constant product formula x * y = k to determine token prices based on the available liquidity in the pool.

Here's how Uniswap V2 addresses slippage and maintains efficient pricing:
1. Constant Product Formula: Uniswap V2 uses the constant product formula to manage liquidity pools. For a pair of tokens (e.g., ETH/DAI), the product of the reserves of the two tokens remains constant x * y = k where x is the quantity of one token, y is the quantity of the other token, and k is a constant.

2. Price Calculation: The price of a token in a Uniswap V2 pool is determined by the ratio of the reserves of the two tokens. For example, if the pool holds ETH and DAI, the price of ETH in terms of DAI is price = y_reserve / x_reserve

3. Impact of Trade Size: When a trade is executed on Uniswap V2, the reserves of the tokens in the pool change based on the trade size. Larger trades can cause greater slippage because they move the price as they are executed due to the constant product formula.

Here's a simplified example of how Uniswap V2 calculates the output amount and addresses slippage:

function getAmountOut(uint amountIn, uint reserveIn, uint reserveOut) internal pure returns (uint amountOut) {
    require(amountIn > 0, "UniswapV2: INSUFFICIENT_INPUT_AMOUNT");
    require(reserveIn > 0 && reserveOut > 0, "UniswapV2: INSUFFICIENT_LIQUIDITY");

    uint amountInWithFee = amountIn * 997;
    uint numerator = amountInWithFee * reserveOut;
    uint denominator = reserveIn * 1000 + amountInWithFee;
    amountOut = numerator / denominator;
}
In this function:

amountIn: The amount of the input token being swapped.
reserveIn: The amount of the input token (e.g., ETH) in the liquidity pool.
reserveOut: The amount of the output token (e.g., DAI) in the liquidity pool.
The getAmountOut function calculates the expected output amount (amountOut) based on the input amount, reserve amounts, and the constant product formula adjusted for a 0.3% fee (997 / 1000).

By using this mechanism, Uniswap V2 aims to minimize slippage by ensuring that traders receive an output amount that closely matches their expectations, factoring in the liquidity available in the pool and the impact of the trade size on the pool's reserves. However, large trades relative to the pool size can still result in significant slippage, especially in less liquid markets.

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution
Preventing Zero or Near-Zero Liquidity Adds: By subtracting a minimum liquidity value (MINIMUM_LIQUIDITY) upon initial minting of liquidity tokens, Uniswap V2 discourages users from creating extremely small or negligible liquidity positions. This minimum threshold ensures that liquidity providers contribute a meaningful amount of liquidity to the pool, which is essential for maintaining efficient trading and price discovery.

Establishing a Base Liquidity Floor: The MINIMUM_LIQUIDITY value acts as a base liquidity floor that all liquidity providers must surpass when adding liquidity for the first time. This helps in maintaining a healthy liquidity pool where each position has a reasonable size relative to the overall pool size.

Protection Against Exploits: Setting a minimum liquidity threshold helps protect the Uniswap V2 protocol against potential exploits or attacks that might attempt to flood the liquidity pool with very small liquidity amounts. Such actions could otherwise disrupt the proper functioning of the automated market maker (AMM) model and impact the accuracy of pricing mechanisms.

Efficient Liquidity Management: By ensuring that all liquidity providers contribute at least a minimum amount of liquidity, Uniswap V2 can more effectively manage and optimize the allocation of liquidity across different token pairs. This supports overall market liquidity and improves the trading experience for users on the platform.

In summary, the subtraction of a minimum liquidity value during the initial minting process in UniswapV2Pair is a deliberate design choice aimed at promoting healthy liquidity provision, safeguarding against potential abuses, and maintaining the integrity and efficiency of the Uniswap V2 decentralized exchange protocol. This approach contributes to the stability and resilience of the liquidity pools and enhances the overall user experience within the ecosystem.

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution
The intention behind the specific formula used when depositing tokens into the UniswapV2Pair contract (not for the first time) is to ensure that the liquidity shares provided by the user accurately reflect the proportional ownership of the token pair within the liquidity pool. This formula is designed to maintain the constant product invariant of the Uniswap V2 automated market maker (AMM) model.

Here's the rationale and intention explained step-by-step:

Maintaining Constant Product Invariant: Uniswap V2 operates on the principle of a constant product market maker model, where the product of the token balances in the liquidity pool remains constant. The product of the token balances (reserve amounts) is represented as reserve0 * reserve1 = k, where reserve0 and reserve1 are the balances of token0 and token1 in the pool, respectively, and k is a constant.

Liquidity Share Calculation: When a user adds liquidity (deposits tokens into the pool), they are issued liquidity tokens representing their share of the total liquidity pool. The number of liquidity tokens received by the user should reflect their proportional contribution to the total liquidity pool value.

Formula to Calculate Liquidity Shares: The specific formula used to calculate liquidity shares is based on the constant product invariant. When a user deposits tokens (not for the first time), the UniswapV2Pair contract calculates the optimal amount of the second token (amount1) required to maintain the constant product after adding amount0 of the first token. This ensures that the product of the updated reserve amounts (reserve0 + amount0 and reserve1 + amount1) remains equal to k.

Intention Behind the Formula: By using this formula, Uniswap V2 ensures that liquidity providers receive liquidity tokens corresponding to their proportional contribution to the liquidity pool's value. This mechanism prevents arbitrage opportunities and maintains the integrity of the pricing mechanism in the AMM, ensuring that users' shares accurately represent the underlying asset's value they contribute to the pool.

In summary, the intention behind using a specific formula for calculating liquidity shares during token deposits in UniswapV2Pair is to preserve the constant product invariant of the AMM model, thereby ensuring fair and efficient pricing and liquidity provision within the decentralized exchange ecosystem. This approach supports the core principles of Uniswap V2's liquidity provision mechanism.

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution
A sandwich attack is a type of front-running exploit that occurs in decentralized exchanges (DEXs) like Uniswap. In this attack, the malicious actor (the attacker) inserts their own transactions before and after a target transaction (initiated by another user), taking advantage of the predictable order of transactions in the Ethereum mempool.

Here's how a sandwich attack works and its potential impact:

Identifying Target Transaction: The attacker monitors the mempool for specific transactions that they can exploit. For example, the attacker might identify a large transaction where a user is swapping a significant amount of tokens.

Front-Running the Target: Before the target transaction is included in a block, the attacker quickly submits their own transaction that exploits the same liquidity pool but in the opposite direction. For instance, if the target transaction is swapping Token A for Token B, the attacker might swap Token B for Token A.

Sandwiching the Target: After placing their own transaction before the target, the attacker follows up with another transaction that further exploits the situation. This second transaction effectively "sandwiches" the target transaction between the attacker's transactions.

Impact on Swap: The impact of a sandwich attack can be significant for the user initiating the swap:

Price Manipulation: By front-running and sandwiching the target transaction, the attacker can impact the price of tokens being swapped, resulting in a less favorable exchange rate for the user.
Higher Slippage: The attacker's transactions can cause increased slippage for the target transaction, leading to a larger difference between the expected price and the actual execution price.
Reduced Gains or Increased Losses: Ultimately, the user initiating the swap may receive fewer tokens than expected or pay more tokens than anticipated due to the manipulated market conditions caused by the sandwich attack.
To mitigate the risk of a sandwich attack when initiating a swap on DEXs like Uniswap:

Use Limit Orders: Some DEX platforms support limit orders, which can help prevent front-running by executing trades only when specific price conditions are met.
Monitor Gas Prices: Keep an eye on gas prices and transaction delays, as these factors can impact the likelihood of being sandwiched.
Utilize Arbitrage Bots: Consider using arbitrage bots or smart contract strategies that can react quickly to market changes and potentially counteract the effects of sandwich attacks.
Overall, while sandwich attacks can pose challenges for traders on decentralized exchanges, being aware of these risks and employing proactive strategies can help mitigate their impact.
