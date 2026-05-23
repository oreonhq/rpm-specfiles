Summary: Produces a document with syntax highlighting
Name: source-highlight
Version: 3.1.9
Release: 27%{?dist}
License: GPL-3.0-or-later AND GFDL-1.1-or-later AND LicenseRef-Fedora-Public-Domain AND GPL-2.0-only AND GPL-3.0-only AND GPL-3.0-or-later WITH Bison-exception-2.2
Source0: https://ftp.gnu.org/gnu/src-highlite/%{name}-%{version}.tar.gz
Source1: https://ftp.gnu.org/gnu/src-highlite/%{name}-%{version}.tar.gz.sig
URL: http://www.gnu.org/software/src-highlite/
# Taken from https://git.savannah.gnu.org/cgit/src-highlite.git/patch/?id=904949c9026cb772dc93fbe0947a252ef47127f4
# and slightly adapted
Patch0: 904949c9026cb772dc93fbe0947a252ef47127f4.patch
Patch1: source-highlight-bz2256374-lesspipe_sh.patch
BuildRequires: make
BuildRequires: bison, flex, boost-devel
BuildRequires: help2man, chrpath, pkgconfig(bash-completion)
BuildRequires: gcc, gcc-c++
%if 0%{!?rhel:1} || 0%{?rhel} < 9
BuildRequires: ctags
Requires: ctags
%endif

%description
This program, given a source file, produces a document with syntax
highlighting. At the moment this package can handle:
Java, Javascript, C/C++, Prolog, Perl, Php3, Python, Flex, ChangeLog, Ruby,
Lua, Caml, Sml and Log as source languages, and HTML, XHTML and ANSI color
escape sequences as output format.


%package devel
Summary: Development files for source-highlight
Requires: %{name}%{?_isa} = %{version}-%{release}
# For linking against source-higlight using pkgconfig
Requires: boost-devel

%description devel
Development files for source-highlight

%prep
%autosetup -p1

%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
%if 0%{?rhel} > 8
export CTAGS=do_not_use_ctags
%endif
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

# Submitted and accepted upstream:
# https://savannah.gnu.org/bugs/index.php?63225
# This can be removed upon next release after 3.1.9
echo -e >> $RPM_BUILD_ROOT%{_datadir}/source-highlight/lang.map \
"\nrpm-spec = spec.lang\n"

bashcompdir=$(pkg-config --variable=completionsdir bash-completion)
mkdir -p $RPM_BUILD_ROOT$bashcompdir
mv $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/source-highlight \
    $RPM_BUILD_ROOT$bashcompdir/
rmdir $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d

%files
%doc docs/source-highlight/*
%{_bindir}/cpp2html
%{_bindir}/java2html
%{_bindir}/source-highlight
%{_bindir}/source-highlight-esc.sh
%{_bindir}/check-regexp
%{_bindir}/source-highlight-settings
%{_bindir}/src-hilite-lesspipe.sh
%{_datadir}/bash-completion/
%{_libdir}/libsource-highlight.so.*
%dir %{_datadir}/source-highlight
%{_datadir}/source-highlight/*
%{_mandir}/man1/*
%{_infodir}/source-highlight*.info*

%files devel
%dir %{_includedir}/srchilite
%{_libdir}/libsource-highlight.so
%{_libdir}/pkgconfig/source-highlight.pc
%{_includedir}/srchilite/*.h

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.1.9-27
- Prepare for Oreon 11 (RP1)
