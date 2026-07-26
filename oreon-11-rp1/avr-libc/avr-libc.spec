%global source0_hash 0af6bf62a4452268cd9588da9e9cc1414d0e7febf3f5ce09c8187426e019717e

# FORCE NOARCH
# This package is noarch intentionally, although it supplies binaries,
# as they're not intended for the build platform, but for AVR.
# The related discussion can be found here:
# https://www.redhat.com/archives/fedora-devel-list/2009-February/msg02261.html
%global _binaries_in_noarch_packages_terminate_build 0

Name:           avr-libc
Version:        2.2.1
Release:        5%{?dist}
Summary:        C library for use with GCC on Atmel AVR microcontrollers
License:        BSD-3-Clause
URL:            https://github.com/avrdudes/avr-libc/
Source0:	https://github.com/avrdudes/avr-libc/releases/download/avr-libc-2_2_0-release/avr-libc-%{version}.tar.bz2
Source1:        http://download.savannah.gnu.org/releases/avr-libc/avr-libc-manpages-%{version}.tar.bz2
Source2:        https://avrdudes.github.io/avr-libc/avr-libc-user-manual-%{version}.tar.bz2
Source3:        https://avrdudes.github.io/avr-libc/avr-libc-user-manual-%{version}.pdf.bz2
Patch0:         avr-libc-1.6.4-documentation.patch
Source5:        http://distribute.atmel.no/tools/opensource/Atmel-AVR-GNU-Toolchain/3.5.4/avr/avr8-headers.zip

BuildRequires:  avr-gcc, autoconf, automake, libtool
BuildRequires: make
BuildArch:      noarch

%description
AVR Libc is a Free Software project whose goal is to provide a high quality C
library for use with GCC on Atmel AVR microcontrollers.

AVR Libc is licensed under a single unified license. This so-called modified
Berkeley license is intented to be compatible with most Free Software licenses
like the GPL, yet impose as little restrictions for the use of the library in
closed-source commercial applications as possible.

%package doc
Summary:        AVR C library docs in html and pdf format
Requires:       %{name} = %{version}-%{release}
Obsoletes:      %{name}-docs < %{version}-%{release}

%description doc
This package contains the AVR C library docs in html and pdf format, the main
package already contains the docs in man-page format (use "avr-man xxxx" to
access these).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# atmel's tarball needs some shuffling to have expected directory layout
# must be done in two steps because of conflicting libc directory
tar -joxf %SOURCE1
%patch -P0 -p1 -b .nolatexbatch

I=0
unzip %{SOURCE5} -d avr8-headers
for i in ./avr8-headers/avr/io[0-9a-zA-Z]*.h
do
  cp $i include/avr/ -v
done

# Add html docs
mkdir html
cd html/
tar -jxvf %SOURCE2
cd -

# Add pdf manual
mkdir pdf
cd pdf/
bzip2 -dc %SOURCE3 > avr-libc-user-manual-%{version}.pdf
cd -

for i in doc/api/faq.dox doc/api/overview.dox include/stdio.h include/stdlib.h;
  do
    iconv -f CP1252 -t UTF8 $i > tmp
    mv tmp $i
done
sed -i 's|@DOC_INST_DIR@/man|%{_prefix}/avr/share/man|' scripts/avr-man.in

%build
#./bootstrap

# really don't try to force distrowide flags on crosscompiled noarch
unset CC CXX CFLAGS CXXFLAGS FFLAGS FCFLAGS LDFLAGS LT_SYS_LIBRARY_PATH

# The ps doc ways in at 7Mb versus 2.5 for the pdf and has little added value
./configure --prefix=%{_prefix} --host=avr --build=`./config.guess` #--enable-doc
# don't use %{?_smp_mflags}, it breaks the build
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# put the man-pages in the FHS mandir and gzip them
mkdir -p $RPM_BUILD_ROOT%{_prefix}/avr/share
find man/ -type f -exec gzip {} \;
mv man  $RPM_BUILD_ROOT%{_prefix}/avr/share

# we only want to use %doc with an absolute path to avoid rpmbuild from erasing
# %{_docdir}/%{name}
mv $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} $RPM_BUILD_ROOT%{_docdir}/%{name}
install -p -m 644 doc/TODO AUTHORS LICENSE NEWS \
  pdf/* README.md $RPM_BUILD_ROOT%{_docdir}/%{name}
mkdir $RPM_BUILD_ROOT%{_docdir}/%{name}/html
cp -ap html/%{name}-user-manual*/* $RPM_BUILD_ROOT%{_docdir}/%{name}/html
chmod -R u=rwX,g=rX,o=rX $RPM_BUILD_ROOT%{_docdir}/%{name}/html

# despite us being noarch redhat-rpm-config insists on stripping our files
%if %{fedora}0 > 200
%global __os_install_post /usr/lib/rpm/brp-compress
%else
%global __os_install_post /usr/lib/rpm/redhat/brp-compress
%endif

%files
%dir %{_prefix}/avr
%dir %{_prefix}/avr/share
%doc %{_prefix}/avr/share/man
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/AUTHORS
%doc %{_docdir}/%{name}/LICENSE
%doc %{_docdir}/%{name}/NEWS
%doc %{_docdir}/%{name}/README.md
%doc %{_docdir}/%{name}/TODO
%doc %{_docdir}/%{name}/examples
%{_prefix}/avr/include
%{_prefix}/avr/lib
%{_bindir}/avr-man

%files doc
%doc %{_docdir}/%{name}/html
%doc %{_docdir}/%{name}/%{name}*.pdf

%changelog
%autochangelog
