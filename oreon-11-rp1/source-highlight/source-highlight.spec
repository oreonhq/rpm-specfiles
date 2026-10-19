%global source1_hash 28954a746a92a7bda2509b0304adc3be38b027f24a7c7015da8cfc28f1bc253f
%global source0_hash 3a7fd28378cb5416f8de2c9e77196ec915145d44e30ff4e0ee8beb3fe6211c91
Summary:        Produces a document with syntax highlighting
Name: source-highlight
Version: 3.1.9
Release:        27%{?dist}
License: GPL-3.0-or-later AND GFDL-1.1-or-later AND LicenseRef-Fedora-Public-Domain AND GPL-2.0-only AND GPL-3.0-only AND GPL-3.0-or-later WITH Bison-exception-2.2
Source0:        https://mirrors.kernel.org/gnu/src-highlite/%{name}-%{version}.tar.gz
Source1:        https://mirrors.kernel.org/gnu/src-highlite/%{name}-%{version}.tar.gz.sig
URL: http://www.gnu.org/software/src-highlite/
Patch0: 904949c9026cb772dc93fbe0947a252ef47127f4.patch
Patch1: source-highlight-bz2256374-lesspipe_sh.patch
# oreon:deps
BuildRequires:  bison
BuildRequires:  boost-devel
BuildRequires:  chrpath
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  pkgconfig(bash-completion)
# /oreon:deps
%description
This program, given a source file, produces a document with syntax
highlighting. At the moment this package can handle:
Java, Javascript, C/C++, Prolog, Perl, Php3, Python, Flex, ChangeLog, Ruby,
Lua, Caml, Sml and Log as source languages, and HTML, XHTML and ANSI color
escape sequences as output format.

%package devel
Summary: Development files for source-highlight
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: boost-devel
%description devel
Development files for source-highlight

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
%configure --disable-static \
           --with-boost-regex=boost_regex
%make_build
%install
%make_install
mv $RPM_BUILD_ROOT%{_datadir}/doc/ docs
%{__sed} -i 's/\r//' docs/source-highlight/*.css
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/source-highlight
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/source-highlight-settings
echo -e >> $RPM_BUILD_ROOT%{_datadir}/source-highlight/lang.map \
"\nrpm-spec = spec.lang\n"
bashcompdir=$(pkg-config --variable=completionsdir bash-completion)
mkdir -p $RPM_BUILD_ROOT$bashcompdir
mv $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/source-highlight \
    $RPM_BUILD_ROOT$bashcompdir/
rmdir $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n source-highlight-devel -f %{oreon_filedir}/source-highlight-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.1.9-27
- Prepare for Oreon 11 (RP1)
