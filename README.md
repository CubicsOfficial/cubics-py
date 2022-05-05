# Official Python Client for Cubics

Official Python client to interact with Cubics Blockchain and Cubics Blockchain Interface.

Cubics is a serverless layer-1 blockchain for Metaverse, Gaming, and NFT applications that provides infinite scalability, high throughput, sub-second confirmation times, and fees at a tenth of a cent. Cubics achieves this by leveraging serverless compute and storage cloud services while innovating incentive structures and extending the Byzantine Fault Tolerance consensus mechanism for scalability.

# General

Install Cubics through pip, import it, generate a public/private key (or use your existing ones) and start building using the examples below.

```
# Installation
pip install cubics

# Imports
import cubics

# Generate and init a keypair
publicKey, privateKey = cubics.crypto.generateKeypair()
cubics.wallet.init(publicKey, privateKey)
```

# Interface

The interface methods allow to interact with storage nodes for read-only functionality. Using these methods, you could build a similar frontend app like our [**network explorer**](https://cubics.network). Interface requests are free, but rate-limited and should allow for "regular" usage. Please contact us at developers@cubics.com if you would like to have dedicated limits.

## Transaction

```
cubics.transaction.poll(hash=hash, interval=number, timeout=number)
cubics.transaction.read(hash=hash)
cubics.transaction.list(hashes=[hash])
cubics.transaction.scanSenderCreated(sender=address)
cubics.transaction.scanPeriodCreated(period=period)
```

## Transfer

```
cubics.transfer.read(hash=hash)
cubics.transfer.list(hashes=[hash])
cubics.transfer.scanSenderCreated(sender=address)
cubics.transfer.scanFromCreated(fromAddress=address)
cubics.transfer.scanToCreated(to=address)
cubics.transfer.scanTokenCreated(token=token)
cubics.transfer.scanFromTokenCreated(fromAddress=address, token=token)
cubics.transfer.scanToTokenCreated(to=address, token=token)
```

## Token

```
cubics.token.read(address=token)
cubics.token.list(addresses=[token])
cubics.token.scanCreatorCreated(creator=address)
cubics.token.scanNameCreated(name=string)
cubics.token.scanSymbolCreated(symbol=string)
cubics.token.scanOwnerCreated(owner=address)
cubics.token.scanContentCreated(content=hash)
cubics.token.scanOwnerCategoryCreated(owner=address, category=string)
cubics.token.scanCreatorCategoryCreated(creator=address, category=string)
```

## Pool

```
cubics.pool.instance(address=pool)
cubics.pool.read(address=pool)
cubics.pool.list(addresses=[pool])
cubics.pool.scanTokenProgramCreated(token=token, program=string)
cubics.pool.scanNameCreated(name=string)
cubics.pool.scanCreatorCreated(creator=address)
cubics.pool.scanProgramCreated(program=string)
cubics.pool.scanProgramExpires(program=string)
cubics.pool.scanProgramNumber(program=string)
cubics.pool.scanProgramBaseBalance(program=string)
cubics.pool.scanProgramTokenBalance(program=string)
cubics.pool.scanProgramTransfersCount(program=string)
```

## Address

```
cubics.address.read(address=address)
```

## Allowance

```
cubics.allowance.read(hash=hash)
cubics.allowance.list(hashes=[hash])
cubics.allowance.readCreatorSpenderToken(creator=address, spender=address, token=token)
cubics.allowance.scanCreatorCreated(creator=address)
cubics.allowance.scanSpenderCreated(spender=address)
```

## Balance

```
cubics.balance.read(hash=hash)
cubics.balance.list(hashes=[hash])
cubics.balance.readAddressToken(address=address, token=token)
cubics.balance.scanAddressAmount(address=address)
cubics.balance.scanTokenAmount(token=token)
```

## Candle

```
cubics.candle.read(interval=interval, token=token, time=time)
cubics.candle.scanIntervalTokenTime(interval=interval, token=token)
cubics.candle.scanIntervalTimeTurnover(interval=interval)
cubics.candle.scanIntervalTimeChange(interval=interval)
```

## Claim

```
cubics.claim.read(hash=hash)
cubics.claim.list(hashes=[hash])
cubics.claim.scanHolderCategoryCreated(holder=address, category=string)
cubics.claim.scanIssuerCategoryCreated(issuer=address, category=string)
cubics.claim.scanIssuerAnswer(issuer=address)
cubics.claim.scanIssuerNumber(issuer=address)
cubics.claim.scanIssuerTokenAmount(issuer=address)
cubics.claim.scanIssuerBaseAmount(issuer=address)
cubics.claim.scanIssuerCreated(issuer=address)
cubics.claim.scanHolderCreated(holder=address)
cubics.claim.scanIssuerTokenCreated(issuer=address, token=token)
cubics.claim.scanHolderTokenCreated(holder=address, token=token)
cubics.claim.scanIssuerHolder(issuer=address, holder=address)
cubics.claim.scanIssuerHolderToken(issuer=address, holder=address, token=token)
```

## Registry

```
cubics.registry.read(hash=hash)
cubics.registry.list(hashes=[hash])
cubics.registry.scanContentCreated(content=string)
cubics.registry.scanFingerprintCreated(fingerprint=string)
cubics.registry.scanClusterCreated(cluster=string)
```

## Search

```
cubics.search.query(query=string)
```

## Statistic

```
cubics.statistic.read(key=key, time=time)
cubics.statistic.scan(key=key)
```

## Wallet

```
cubics.wallet.init(publicKey=hash, privateKey=hash)
cubics.wallet.managed(account=string, secret=string, unsafe=boolean, create=boolean)
cubics.credentials.sign(account=string, secret=string, tx=transaction)
```

# Modules

Modules are wrapper methods that submit transactions to the network endpoint. Fees for methods are fixed and most recent fees can be found on [docs.cubics.com](https://docs.cubics.com). 


## Transfer

```
cubics.transfer.create(to=address, token=token, amount=amount, fromAddress=address)
```

## Token

```
cubics.token.create(name=string, symbol=string, supply=amount, reserve=amount, description=string, links=[string], meta=object, preview=url, owner=address, frozen=boolean, category=string, object=url, mime=string, content=string)
Cubics.token.update(name=string, description=string, links=[string], meta=object, preview=url, owner=address, frozen=boolean, category=string, mime=string)
Cubics.token.mint(token=token, amount=amount)
```

## Pool

For pool creation, it is recommended to use the program-specific methods (which are wrappers around this method). Available pool programs are auction, launch, lock, loot, lottery, royalty, staking, swap, vote.

```
cubics.pool.create(token=token, program=string, expires=timestamp)
```

## Claim
```
cubics.claim.create(owner=address, token=token, tokenAmount=amount, expires=timestamp)
cubics.claim.update(claim=claim, tokenAmount=amount)
cubics.claim.transfer(claim=claim, to=address)
cubics.claim.resolve(claim=claim)
```

## Profile

```
cubics.profile.update(name=string, description=string, links=[string], meta=object, preview=url, category=string)
```

## Allowance

```
cubics.allowance.update(token=token, spender=spender, amount=amount)
```

## Transaction
Approx. 10 instructions can be batched into one request. The exact number depends on reads & writes, and sub-calls made by each instruction. It is required that all instructions have the tx=False flag, to be returned as instruction object. Batch instructions are processed atomically, meaning that if one instruction fails, the transaction throws an error and no instruction is processed.

```
cubics.transaction.submit([
    cubics.transfer.create(to=address, token=token, amount=amount, tx=False),
    cubics.transfer.create(to=address, token=token, amount=amount, tx=False),
    cubics.token.create(name=string, symbol=string, supply=amount, tx=False),
    cubics.token.create(name=string, tx=False),
    cubics.token.create(name=string, tx=False),
])
```

# Programs

Pools are based on programs, which are pre-written smart contracts on Cubics. For further details on individual functionalities or requirements check out the [Cubics Docs](https://docs.cubics.com). To get the pool object from pool-address, use the cubics.pool.instance interface method.

## Auction

```
# Creator methods:
auction = cubics.pool.create(program='auction', token=token, expires=timestamp, cubicsTarget=amount, cubicsLimit=amount)
auction.deposit()
auction.close()

# Participant methods:
auction.transfer(amount=amount)
auction.resolve()
auction.cancel()
```

## Launch

```
# Creator methods:
launch = cubics.pool.create(program='launch', token=token, expires=timestamp, baseTarget=amount, baseLimit=amount)
launch.deposit(amount=amount)
launch.withdraw(claim=claim)
launch.close()

# Participant methods:
launch.resolve()
launch.transfer(amount=amount)
launch.claim(claim=claim)
```

## Lending

```
# Creator methods:
lending = cubics.pool.create(program='lending', token=token)
lending.deposit(amount=amount)
lending.withdraw(claim=claim)

# Participant methods:
lending.liquidate(claim=claim)
lending.transfer(amount=amount, collateralization=number)
lending.settle(claim=claim)
```

## Lock

```
# Creator methods:
lock = cubics.pool.create(program='lock', token=token, expires=timestamp)

# Participant methods:
lock.transfer(amount=amount, unlocks=timestamp, address=address)
lock.claim(claim=claim)
```

## Loot

```
# Creator methods:
loot = cubics.pool.create(program='loot', token=token, probability=number, minAmount=amount, maxAmount=amount)
loot.deposit(token=token)
loot.withdraw(claim=claim)
loot.clear()

# Participant methods:
loot.transfer()
```

## Lottery

```
# Creator methods:
lottery = cubics.pool.create(program='lottery', token=token, expires=timestamp, claimsLimit=integer, transfersLimit=integer)
lottery.deposit(amount=amount)
lottery.withdraw(claim=claim)
lottery.close()
lottery.clear()

# Participant methods:
lottery.transfer()
lottery.claim(claim=claim)
lottery.resolve()
```

## Royalty

```
# Creator methods:
royalty = cubics.pool.create(program='royalty', token=token, rate=number)
royalty.deposit(amount=amount)
royalty.withdraw(claim=claim)
royalty.close()

# Participant methods:
royalty.transfer(token=token)
royalty.claim(token=token)
```

## Staking

```
# Creator methods:
staking = cubics.pool.create(program='staking', token=token, rate=number, percentage=number, minTime=integer, maxTime=integer, minAmount=amount, maxAmount=amount)
staking.deposit(amount=amount)
staking.withdraw(claim=claim)

# Participate methods:
staking.transfer(amount=amount, unlocks=timestamp)
staking.claim(claim=claim)
```

## Swap

Swap pools are automatically created for all fungible tokens, with the same pool-address as the token-address.

```
# Liquidity provider methods:
swap.deposit(tokenAmount=amount, baseAmount=amount, unlocks=timestamp)
swap.withdraw(claim=claim, percentage=number)

# Participant methods:
swap.transfer(token=token, amount=amount)
```

## Vote

```
# Creator methods:
vote = cubics.pool.create(program='vote', token=token, expires=timestamp, mechanism=string, maxAmount=amount, candidates=[string])
cubics.vote.oracle(answer=answer)

# Participant methods:
vote.transfer(amount=amount, answer=string, number=number)
vote.resolve()
vote.claim(claim=claim)
```

# Feedback & Contributions

We encourage contributions to this library. Please also join our social channels in case you have suggestions or require technical help.

[**Website**](https://cubics.com)
[**Twitter**](https://twitter.com/CubicsOfficial)
[**Telegram**](https://t.me/CubicsOfficial)