import { TezosToolkit } from '@taquito/taquito';
import { InMemorySigner } from '@taquito/signer';
const Tezos = new TezosToolkit('http://localhost:20000');

Tezos.setProvider({
  signer: new InMemorySigner('edsk3QoqBuvdamxouPhin7swCvkQNgq4jP5KZPbwWNnwdZpSpJiEbq'),
});

Tezos.contract
  .at('KT1Apz7MZhXoUZ455JJ4in6WrSW3GCSjfV7v')
  .then((contract) => {
    return contract.methods.double().send();
  })
  .then((op) => {
    // println(`Waiting for ${op.hash} to be confirmed...`);
    return op.confirmation(1).then(() => op.hash);
  })
  .then((hash) => console.log(`Operation injected: ${hash}`))
  .catch((error) => console.log(`Error: ${JSON.stringify(error, null, 2)}`));