%global source0_hash 84b1493efe967e85070c69e78b04dc55edc5c5718f9d6b77929762cb2abed278

%bcond_with bootstrap

Name:           ragel
Version:        7.0.4
Release:        9%{?dist}
Summary:        Finite state machine compiler

# aapl/ is the LGPLv2+
# Automatically converted from old format: MIT and LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-LGPLv2+
URL:            http://www.colm.net/open-source/%{name}/
Source0:        https://www.colm.net/files/%{name}/%{name}-%{version}.tar.gz
# allow building without *.la for libcolm and libfsm
Patch:          https://github.com/adrian-thurston/ragel/commit/463f4914057b0193c6ca025e9233c17035bc0448.patch#/ragel-fallback-no-la.diff
Patch:          ragel-use-libdir.diff

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
# for manual
BuildRequires:  asciidoc
BuildRequires:  dblatex
BuildRequires:  texlive-latex
BuildRequires:  texlive-upquote
BuildRequires:  transfig
%if %{with bootstrap}
BuildRequires:  kelbt
BuildRequires:  ragel
%endif
BuildRequires:  colm-devel = 0.14.7

# Unfortunately, upstream doesn't exist and not possible to find version
Provides:       bundled(aapl)
# ragel no longer ships include files since libfsm is moved to colm
Obsoletes:      ragel-devel < 7.0.4-1

%description
Ragel compiles executable finite state machines from regular languages.
Ragel targets C, C++ and ASM. Ragel state machines can not only recognize
byte sequences as regular expression machines do, but can also execute code
at arbitrary points in the recognition of a regular language. Code embedding
is done using inline operators that do not disrupt the regular language syntax.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
# Do not pollute with docs
sed -i -e "/dist_doc_DATA/d" Makefile.am

%build
autoreconf -vfi
%configure --disable-static --with-colm=%{_prefix}
%make_build

%install
%make_install
find %{buildroot}%{_libdir} -type f -name '*.la' -print -delete
install -p -m 0644 -D %{name}.vim %{buildroot}%{_datadir}/vim/vimfiles/syntax/%{name}.vim

%ldconfig_scriptlets

%files
%license COPYING
%doc ragel-guide.html ragel-guide.pdf
%{_bindir}/%{name}
%{_bindir}/%{name}-*
%{_mandir}/man1/%{name}.1*
%exclude %{_libdir}/libragel.so
%{_libdir}/libragel.so.*
%{_datarootdir}/%{name}.lm
%{_datarootdir}/out-go.lm
%dir %{_datadir}/vim
%dir %{_datadir}/vim/vimfiles
%dir %{_datadir}/vim/vimfiles/syntax
%{_datadir}/vim/vimfiles/syntax/%{name}.vim

%changelog
%autochangelog
