one directory to rule them all
==============================

For more information, see the 
[proposal](https://fedoraproject.org/Changes/Web_Assets) and 
[proposed guidelines](https://fedoraproject.org/User:Patches/PackagingDrafts/Web_Assets)

Try Me
------

```sh
sudo yum install git fedora-packager
git clone https://github.com/tchollingsworth/fedora-web-assets
cd fedora-web-assets
fedpkg --dist=f19 local
sudo yum install noarch/*
```

[There are also some builds here.](http://patches.fedorapeople.org/web-assets/)
