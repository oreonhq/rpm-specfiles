
Autor : Frederic Labbe
Mail  : fred@frederic-labbe.com (privat)
      : frederic.labbe@ch-avranches-granville.fr (prof)

ooo2txt can convert OpenOffice.org file into text.
ooo2txt is write with perl 5.
ooo2txt is under LPGL Licence

in order to run ooo2txt.pl you have to install pre-requise perl-module :

1) Requires: perl 5.003_96 or greater 
2) IO::Seekable : supply seek based methods for I/O objects
3) IO::File : supply object methods for filehandles
4) File::Spec : portably perform operations on file names
5) ExtUtils::MakeMaker : create an extension Makefile
6) Compress::Zlib : Interface to zlib compression library
7) Archive::Zip : Provide an interface to ZIP archive files
8) XML:UM : Convert UTF-8 strings to any encoding supported by XML::Encoding

you can download all requires modules at :

http://ooo2txt.fr.st/download/cpan/

ooo2txt permet de convertir des fichiers OpenOffice.org en texte.
ooo2txt est ecrit en perl 5.
ooo2txt est sous licence LGPL.

Pour faire fonctionner ooo2txt.pl vous devez au prealable installer des
modules perl.

1) Requires: perl 5.003_96 or greater 
2) IO::Seekable : supply seek based methods for I/O objects
3) IO::File : supply object methods for filehandles
4) File::Spec : portably perform operations on file names
5) ExtUtils::MakeMaker : create an extension Makefile
6) Compress::Zlib : Interface to zlib compression library
7) Archive::Zip : Provide an interface to ZIP archive files
8) XML:UM : Convert UTF-8 strings to any encoding supported by XML::Encoding

Les modules 2, 3 et 4 sont probablement deja installes mais je preferre
les mentionner car ils sont obligatoires.
sur ma machine linux (mandrake 8.1), je n'ai du installer que les modules
5, 6 et 7 car les autres etaient deja present.
Vous pourrez telecharger tous ces modules sur http://ooo2txt.fr.st/download/cpan/

Si vous utilisez ooo2txt, envoyez moi vos remarques par mail, cela fait 
toujours plaisir. ;-)

Fred.