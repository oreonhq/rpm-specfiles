use ExtUtils::MakeMaker;
WriteMakefile(
    NAME    =>  'TestML',
    test    =>  {TESTS => 'test/*.tml'}
);
