%global source0_hash 6676ff3c37f4958615906dae6c03ecd24c40509fd85c06acc98f55fa77e2d61c
Name:           lowdown
Version:        3_1_1
Release:        1%{?dist}
Summary:        Simple markdown translator
License:        ISC AND BSD-3-Clause AND MIT
URL:            https://kristaps.bsd.lv/lowdown/
%global github_version_tag %(tr '.' '_' <<<VERSION_%{version})
Source0:        https://github.com/kristapsdz/%{name}/archive/%{github_version_tag}/%{name}-%{version}.tar.gz
Patch:          0001-Makefile-link-lowdown-dynamically-and-lowdown-diff-s.patch
Patch:          0001-Makefile-use-standard-make-syntax.patch
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%global soversion 2
%global _docdir_fmt %{name}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libbsd-devel
BuildRequires:  make
# /oreon:deps
%description
Lowdown is a Markdown translator producing HTML5, roff documents in the ms and
man formats, LaTeX, gemini, and terminal output.

Beyond traditional Markdown syntax support, lowdown supports the following
Markdown features and extensions:
  * autolinking
  * fenced code
  * tables
  * superscripts
  * footnotes
  * disabled inline HTML
  * "smart typography"
  * metadata
  * commonmark (in progress)
  * definition lists
  * extended attributes
  * task lists

%package libs
Summary:       %{summary} library
%description libs
This package provides the %{summary}.

%package devel
Summary:       %{summary} header files
Requires:      %{name}-libs = %{version}-%{release}
%description devel
This package provides the %{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n lowdown-%{github_version_tag} -p1

%build

./configure \
  PREFIX=%{_prefix} \
  LIBDIR=%{_libdir} \
  MANDIR=%{_mandir} \
  LDADD='-lbsd'
sed -i "s!^LDFLAGS.*!LDFLAGS = $LDFLAGS!" Makefile.configure 
%make_build
%install
%make_install install_lib_common install_shared
chmod 0755 %{buildroot}%{_bindir}/lowdown
ln -fs lowdown %{buildroot}%{_bindir}/lowdown-diff
chmod 0755 %{buildroot}%{_libdir}/liblowdown.so.%{soversion}
find %{buildroot} -type f -exec chmod u+w {} \;
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

LD_LIBRARY_PATH=%{buildroot}%{_libdir} \
  make regress
%files -f %{oreon_filedir}/main.list
%files -n lowdown-libs -f %{oreon_filedir}/lowdown-libs.list
%files -n lowdown-devel -f %{oreon_filedir}/lowdown-devel.list

%changelog

%autochangelog
