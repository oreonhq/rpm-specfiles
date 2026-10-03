%global source0_hash 6037b31c358dda6f580f7321f97a182144a8401c690b458fcae055c65501977d

Name:           colm
Version:        0.14.7
Release:        12%{?dist}
Summary:        Programming language designed for the analysis of computer languages

# aapl/ and some headers from src/ are the LGPLv2+
# Automatically converted from old format: MIT and LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-LGPLv2+
URL:            https://www.colm.net/open-source/colm/
Source0:        https://www.colm.net/files/%{name}/%{name}-%{version}.tar.gz
Patch0:		fc61ecb3a22b89864916ec538eaf04840e7dd6b5.diff
# backport commit that allows AC_CHECK_LIB to detect libfsm
Patch1:         https://github.com/adrian-thurston/colm/commit/28b6e0a01157049b4cb279b0ef25ea9dcf3b46ed.patch#/%{name}-libfsm-ac_check_lib.diff
# Correctly use off_t in cookie_seek_function_t in src/stream.c
Patch2:         colm-0.14.7-ac_sys_largefile-for-off_t.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  asciidoc

# Unfortunately, upstream doesn't exist and not possible to find version
Provides:       bundled(aapl)

%description
Colm is a programming language designed for the analysis and transformation
of computer languages. Colm is influenced primarily by TXL. It is
in the family of program transformation languages.

%package devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Do not pollute with docs
sed -i -e "/dist_doc_DATA/d" Makefile.am
# Remove incompatible SIZEOF_LONG definition
sed -i -e '\@SIZEOF_LONG@d' test/rlparse.d/config.h

%build
autoreconf -vfi
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot}%{_libdir} -type f -name '*.la' -print -delete
install -p -m 0644 -D %{name}.vim %{buildroot}%{_datadir}/vim/vimfiles/syntax/%{name}.vim

%ldconfig_scriptlets

%files
%license COPYING
%doc README
%{_bindir}/%{name}*
%{_libdir}/lib%{name}-%{version}.so
%dir %{_datadir}/vim
%dir %{_datadir}/vim/vimfiles
%dir %{_datadir}/vim/vimfiles/syntax
%{_datadir}/vim/vimfiles/syntax/%{name}.vim
%{_datadir}/doc/%{name}/*
%{_datadir}/*.lm
%{_datadir}/runtests

%files devel
%{_libdir}/lib%{name}.so
%{_libdir}/libfsm*
%{_includedir}/%{name}/
%{_includedir}/libfsm*
%{_includedir}/aapl*

%changelog
%autochangelog
