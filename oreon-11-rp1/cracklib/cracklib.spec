%global source1_hash 1d9dd4d8eed30520d83c0f331ac8ddad5b0c78b9fe8a4f456edbba7b6f871250
%global source0_hash 877b823198eb29aa1778b16a70cad05f7b54b164b3bf7ab656fc326c393f4c85
%define dictdir %{_datadir}/cracklib
%define dictpath %{dictdir}/pw_dict
Summary:        A password-checking library
Name: cracklib
Version: 2.10.3
Release:        1%{?dist}
URL: https://github.com/cracklib/cracklib
License: LGPL-2.1-or-later
Source0:        https://github.com/cracklib/cracklib/releases/download/v%{version}/cracklib-%{version}.tar.gz
Source1:        https://github.com/cracklib/cracklib/releases/download/v%{version}/cracklib-words-%{version}.gz
Source2: cracklib.default.zh_CN.po
Source3: missing-words.gz
Conflicts: cracklib-dicts < 2.8
Requires: gzip
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gettext-autopoint
BuildRequires:  make
BuildRequires:  words
BuildRequires:  zlib-devel
# /oreon:deps
%description
CrackLib tests passwords to determine whether they match certain
security-oriented characteristics, with the purpose of stopping users
from choosing passwords that are easy to guess. CrackLib performs
several tests on passwords: it tries to generate words from a username
and gecos entry and checks those words against the password; it checks
for simplistic patterns in passwords; and it checks for the password
in a dictionary.

CrackLib is actually a library containing a particular C function
which is used to check the password, as well as other C
functions. CrackLib is not a replacement for a passwd program; it must
be used in conjunction with an existing passwd program.

Install the cracklib package if you need a program to check users'
passwords to see if they are at least minimally secure. If you install
CrackLib, you will also want to install the cracklib-dicts package.

%package devel
Summary: Development files needed for building applications which use cracklib
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The cracklib-devel package contains the header files and libraries needed
for compiling applications which use cracklib.

%package dicts
Summary: The standard CrackLib dictionaries
BuildRequires: words >= 2-13
BuildRequires: make
Requires: cracklib = %{version}-%{release}
%description dicts
The cracklib-dicts package includes the CrackLib dictionaries.
CrackLib will need to use the dictionary appropriate to your system,
which is normally put in /usr/share/dict/words. Cracklib-dicts also
contains the utilities necessary for the creation of new dictionaries.

If you are installing CrackLib, you should also install cracklib-dicts.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p 1 

# Replace zn_CN.po with one that wasn't mis-transcoded at some point.
install -p -m 644 %{SOURCE2} po/zh_CN.po

mkdir cracklib-dicts
for dict in %{SOURCE3} %{SOURCE1}
do
        cp -fv ${dict} cracklib-dicts/
done
chmod +x util/cracklib-format

%build

sed -i 's,util/cracklib-check <,util/cracklib-check $(DESTDIR)/$(DEFAULT_CRACKLIB_DICT) <,' Makefile.in
%configure --with-pic \
 --without-python \
 --with-default-dict=%{dictpath} --disable-static
make -C po update-gmo
make
%install
%make_install 'pythondir=${pyexecdir}'
./util/cracklib-format cracklib-dicts/* | \
./util/cracklib-packer %{buildroot}%{dictpath}
./util/cracklib-format %{buildroot}%{dictdir}/cracklib-small | \
./util/cracklib-packer %{buildroot}%{dictdir}/cracklib-small
rm -f %{buildroot}%{dictdir}/cracklib-small
sed s,/usr/lib/cracklib_dict,%{dictpath},g lib/crack.h > %{buildroot}%{_includedir}/crack.h
ln -s cracklib-format %{buildroot}%{_sbindir}/mkdict
touch %{buildroot}/top
toprelpath=..
touch %{buildroot}/top
while ! test -f %{buildroot}%{_libdir}/$toprelpath/top ; do
	toprelpath=../$toprelpath
done
rm -f %{buildroot}/top
if test %{dictpath} != %{_libdir}/cracklib_dict ; then
ln -s $toprelpath%{dictpath}.hwm %{buildroot}%{_libdir}/cracklib_dict.hwm
ln -s $toprelpath%{dictpath}.pwd %{buildroot}%{_libdir}/cracklib_dict.pwd
ln -s $toprelpath%{dictpath}.pwi %{buildroot}%{_libdir}/cracklib_dict.pwi
fi
rm -f %{buildroot}%{_libdir}/python*/site-packages/_cracklib*.*a
rm -f %{buildroot}%{_libdir}/libcrack.la
mkdir -p %{buildroot}%{_mandir}/man{3,8}
install -p -m644 doc/*.3 %{buildroot}%{_mandir}/man3/
install -p -m644 doc/*.8 %{buildroot}%{_mandir}/man8/
if ! test -s %{buildroot}%{_mandir}/man8/cracklib-packer.8 ; then
    echo .so man8/cracklib-format.8 > %{buildroot}%{_mandir}/man8/cracklib-packer.8
fi
if ! test -s %{buildroot}%{_mandir}/man8/cracklib-unpacker.8 ; then
    echo .so man8/cracklib-format.8 > %{buildroot}%{_mandir}/man8/cracklib-unpacker.8
fi
%find_lang %{name}
%oreon_autofiles cracklib-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles cracklib-dicts usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test DESTDIR=%{buildroot}
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n cracklib-devel -f %{oreon_filedir}/cracklib-devel.list
%files -n cracklib-dicts -f %{oreon_filedir}/cracklib-dicts.list

%changelog

%autochangelog
