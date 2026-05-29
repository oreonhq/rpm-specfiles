%global source0_hash none

%global source2_key_fpr F7774FB1AD074A7E8C8767EA91738F73E1B768A0

# Conditionalize Ocaml support.  This looks ass-backwards, but it's not.
%ifarch %{ix86}
%bcond_with ocaml
%else
%bcond_without ocaml
%endif

# Verify tarball signature with GPGv2.
%global verify_tarball_signature 1

Name:           hivex
Version:        1.3.24
Release:        14%{?dist}
Summary:        Read and write Windows Registry binary hive files

License:        LGPL-2.1-only AND LGPL-2.0-or-later AND GPL-2.0-or-later
URL:            http://libguestfs.org/

Source0:        http://libguestfs.org/download/hivex/hivex-1.3.24.tar.gz
%if 0%{verify_tarball_signature}
Source1:        hivex-1.3.24.tar.gz.sig
%endif

# Keyring used to verify tarball signature.
%if 0%{verify_tarball_signature}
Source2:       libguestfs.keyring
%endif

BuildRequires:  make
BuildRequires:  autoconf, automake, libtool, gettext-devel
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  %{_bindir}/pod2html
BuildRequires:  %{_bindir}/pod2man
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(IO::Stringy)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
%if %{with ocaml}
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib-devel
%endif
BuildRequires:  python3-devel
BuildRequires:  ruby-devel
BuildRequires:  rubygem-rake
# see also RHBZ#1325022
BuildRequires:  rubygem(json)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(rdoc)
BuildRequires:  readline-devel
BuildRequires:  libxml2-devel
%if 0%{verify_tarball_signature}
BuildRequires:  gnupg2
%endif

Requires:       %{name}-libs = %{version}-%{release}

Conflicts:      %{name} < 1.3.20-6
Obsoletes:      %{name} < 1.3.20-6


%description
Hive files are the undocumented binary files that Windows uses to
store the Windows Registry on disk.  Hivex is a library that can read
and write to these files.

'hivexsh' is a shell you can use to interactively navigate a hive
binary file.

'hivexregedit' (in perl-hivex) lets you export and merge to the
textual regedit format.

'hivexml' can be used to convert a hive file to a more useful XML
format.

In order to get access to the hive files themselves, you can copy them
from a Windows machine.  They are usually found in
%%systemroot%%\system32\config.  For virtual machines we recommend
using libguestfs or guestfish to copy out these files.  libguestfs
also provides a useful high-level tool called 'virt-win-reg' (based on
hivex technology) which can be used to query specific registry keys in
an existing Windows VM.

For OCaml bindings, see 'ocaml-hivex-devel'.

For Perl bindings, see 'perl-hivex'.

For Python 3 bindings, see 'python3-hivex'.

For Ruby bindings, see 'ruby-hivex'.


%package libs
Summary:        Library for %{name}
License:        LGPL-2.1-only AND LGPL-2.0-or-later
Conflicts:      %{name} < 1.3.20-6
Obsoletes:      %{name} < 1.3.20-6


%description libs
%{name}-libs contains the library for %{name}.


%package devel
Summary:        Development tools and libraries for %{name}
Requires:       %{name}-libs = %{version}-%{release}
Requires:       pkgconfig


%description devel
%{name}-devel contains development tools and libraries
for %{name}.


%if !0%{?rhel}
%package static
Summary:        Statically linked library for %{name}
License:        LGPL-2.1-only AND LGPL-2.0-or-later
Requires:       %{name}-devel = %{version}-%{release}


%description static
%{name}-static contains the statically linked library
for %{name}.
%endif


%if %{with ocaml}
%package -n ocaml-%{name}
Summary:       OCaml bindings for %{name}
License:       LGPL-2.0-or-later
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}


%description -n ocaml-%{name}
ocaml-%{name} contains OCaml bindings for %{name}.

This is for toplevel and scripting access only.  To compile OCaml
programs which use %{name} you will also need ocaml-%{name}-devel.


%package -n ocaml-%{name}-devel
Summary:       OCaml bindings for %{name}
License:       LGPL-2.0-or-later
Requires:      ocaml-%{name}%{?_isa} = %{version}-%{release}
Requires:      %{name}-devel%{?_isa} = %{version}-%{release}


%description -n ocaml-%{name}-devel
ocaml-%{name}-devel contains development libraries
required to use the OCaml bindings for %{name}.
%endif


%package -n perl-%{name}
Summary:       Perl bindings for %{name}
License:       LGPL-2.0-or-later AND GPL-2.0-or-later
Requires:      %{name}-libs = %{version}-%{release}


%description -n perl-%{name}
perl-%{name} contains Perl bindings for %{name}.


%package -n python3-%{name}
Summary:       Python 3 bindings for %{name}
License:       LGPL-2.0-or-later
Requires:      %{name}-libs = %{version}-%{release}

%description -n python3-%{name}
python3-%{name} contains Python 3 bindings for %{name}.


%package -n ruby-%{name}
Summary:       Ruby bindings for %{name}
License:       LGPL-2.0-or-later
Requires:      %{name}-libs = %{version}-%{release}
Requires:      ruby(release)
Requires:      ruby
Provides:      ruby(hivex) = %{version}

%description -n ruby-%{name}
ruby-%{name} contains Ruby bindings for %{name}.


%prep
%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%if 0%{verify_tarball_signature}
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif
%setup -q
%autopatch -p1

autoreconf -fi


%build
%configure \
    PYTHON=%{__python3} \
%if !%{with ocaml}
    --disable-ocaml \
%endif
%if 0%{?rhel}
    --disable-static \
%endif
    %{nil}
make V=1 INSTALLDIRS=vendor %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALLDIRS=vendor

# Remove unwanted libtool *.la file:
rm $RPM_BUILD_ROOT%{_libdir}/libhivex.la

# Remove unwanted Perl files:
find $RPM_BUILD_ROOT -name perllocal.pod -delete
find $RPM_BUILD_ROOT -name .packlist -delete
find $RPM_BUILD_ROOT -name '*.bs' -delete

# Remove unwanted Python files:
rm $RPM_BUILD_ROOT%{python3_sitearch}/libhivexmod.la

%find_lang %{name}


%check
if ! make check -k; then
    for f in $( find -name test-suite.log | xargs grep -l ^FAIL: ); do
        echo
        echo "***" $f "***"
        cat $f
        echo
    done
    exit 1
fi

%files -f %{name}.lang
%doc README.md
%license LICENSE
%{_bindir}/hivexget
%{_bindir}/hivexml
%{_bindir}/hivexsh
%{_mandir}/man1/hivexget.1*
%{_mandir}/man1/hivexml.1*
%{_mandir}/man1/hivexsh.1*


%files libs
%doc README.md
%license LICENSE
%{_libdir}/libhivex.so.*


%files devel
%license LICENSE
%{_libdir}/libhivex.so
%{_mandir}/man3/hivex.3*
%{_includedir}/hivex.h
%{_libdir}/pkgconfig/hivex.pc


%if !0%{?rhel}
%files static
%license LICENSE
%{_libdir}/libhivex.a
%endif


%if %{with ocaml}
%files -n ocaml-%{name}
%doc README.md
%dir %{_libdir}/ocaml/hivex
%{_libdir}/ocaml/hivex/META
%{_libdir}/ocaml/hivex/*.cma
%{_libdir}/ocaml/hivex/*.cmi
%{_libdir}/ocaml/stublibs/*.so
%{_libdir}/ocaml/stublibs/*.so.owner


%files -n ocaml-%{name}-devel
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/hivex/*.cmxa
%{_libdir}/ocaml/hivex/*.cmx
%endif
%{_libdir}/ocaml/hivex/*.a
%{_libdir}/ocaml/hivex/*.mli
%endif


%files -n perl-%{name}
%{perl_vendorarch}/*
%{_mandir}/man3/Win::Hivex.3pm*
%{_mandir}/man3/Win::Hivex::Regedit.3pm*
%{_bindir}/hivexregedit
%{_mandir}/man1/hivexregedit.1*


%files -n python3-%{name}
%{python3_sitearch}/hivex/
%{python3_sitearch}/*.so


%files -n ruby-%{name}
%doc ruby/doc/site/*
%{ruby_vendorlibdir}/hivex.rb
%{ruby_vendorarchdir}/_hivex.so


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.24-14
- Prepare for Oreon 11 (RP1)
