%global source0_hash f970b23ae1092872c29177f885f25a1076f1383d930acd032934cee339e1c1d7
Name:       diffmark
Version:    0.10
Release:        1%{?dist}
Summary:        XML diff and merge
License:    diffmark AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
SourceLicense: %{license} AND FSFUL AND FSFULLR AND FSFULLRWD AND X11 AND GPL-2.0-or-later WITH Libtool-exception AND GPL-2.0-or-later WITH Autoconf-exception-generic
URL:        http://www.mangrove.cz/%{name}/
Source0:        http://www.mangrove.cz/%{name}/%{name}-%{version}.tar.gz
Patch0:     %{name}-0.09-remove_rpath.patch
Patch1:     %{name}-gcc11.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  findutils
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  make
# /oreon:deps
%description
This is an XML diff and merge package. It consists of a shared library and
two utilities: dm and dm-merge. 

%package        devel
Summary:        Development files for %{name} library
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
Header files and libraries for developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# automake -i -f to support aarch64, bug #925255
libtoolize --force && autoreconf -i -f

%build

%configure --enable-shared --disable-static
%{make_build}
%install
%{make_install}
find "$RPM_BUILD_ROOT" -name '*.la' -delete
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n diffmark-devel -f %{oreon_filedir}/diffmark-devel.list

%changelog

%autochangelog
