# ST2 Yetibot Pack

Provides a rule to listen for `core.st2.generic.notifytrigger` triggers. Use in
conjunction with:

- [Yetibot](github.com/devth/yetibot)
- [yetibot-stackstorm](https://github.com/devth/yetibot-stackstorm) plugin

## Install

Note the use of `subtree`!

```
st2 run packs.install subtree=true packs=yetibot repo_url=https://github.com/devth/st2-yetibot-pack.git
```

## Config

```
st2 key set yetibot_endpoint <endpoint>
```

## License

Copyright © 2015 Trevor C. Hartman

Distributed under the Eclipse Public License version 1.0.
