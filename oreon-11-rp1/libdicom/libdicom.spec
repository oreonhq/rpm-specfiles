%global source0_hash 75f1167f5153c659cdd58f2b432d2592bf0477abe0087e195bc621b5594ef10a
Name:           libdicom
Version:        1.3.0
Release:        1%{?dist}
Summary:        C library and tools for reading DICOM data sets
License:        MIT
URL:            https://github.com/ImagingDataCommons/%{name}
Source0:        https://github.com/ImagingDataCommons/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(check)
BuildRequires:  uthash-static
# /oreon:deps
%description
libdicom is a C library and a set of tools for reading files that
follow the DICOM medical imaging standard.  It allows random access to
individual frame items of Pixel Data elements, permitting efficient
processing of large DICOM images.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
%description    doc
The %{name}-doc package contains documentation for developing
applications that use %{name}.

%package        tools
Summary:        Tools for decoding DICOM files
%description    tools
The %{name}-tools package contains tools for decoding DICOM files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
mv doc/source doc/text
rm doc/text/conf.py
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n libdicom-devel -f %{oreon_filedir}/libdicom-devel.list
%files -n libdicom-doc -f %{oreon_filedir}/libdicom-doc.list
%files -n libdicom-tools -f %{oreon_filedir}/libdicom-tools.list

%changelog

%autochangelog
