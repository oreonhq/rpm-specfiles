%global source0_hash b251552f6156f26db78fe542179ecfc7b8af0372ef0c9852eb30cdd1dcf54103
Name:           remake
Version:        0.16
Release:        1%{?dist}
Summary:        Build system that bridges the gap between make and redo
License:        GPL-3.0-or-later
URL:            https://github.com/silene/remake
VCS:            git:%{url}.git
Source0:        https://github.com/silene/%{name}/archive/%{name}-%{version}.tar.gz
Patch:          %{name}-test.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  doxygen-latex
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  inotify-tools
BuildRequires:  tex-epstopdf
BuildRequires:  urw-base35-fonts
# /oreon:deps
%description
Remake is a build system with features of both make and redo.  See the
documentation for details on usage and control file syntax.

%package doc
License:        GPL-3.0-or-later AND GPL-1.0-or-later AND MIT
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
Provides:       bundled(js-jquery) = 3.6.0
%description doc
Documentation for using and developing %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n %{name}-%{name}-%{version}

%build

g++ %{build_cxxflags} -D_GNU_SOURCE -o remake remake.cpp %{build_ldflags}
doxygen
%install
mkdir -p %{buildroot}%{_bindir}
install -pm 0755 remake %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -a doxydoc/html %{buildroot}%{_docdir}/%{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

cd testsuite
%ifarch s390x
rm t009.sh
%endif
./all.sh
%files -f %{oreon_filedir}/main.list
%files -n remake-doc -f %{oreon_filedir}/remake-doc.list

%changelog

%autochangelog
