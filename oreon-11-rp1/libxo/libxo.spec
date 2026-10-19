%global source0_hash d12249ffad3ef04b160e6419adf1bbe7e593a60bb23f0a0a077fa780b214934a
Name:           libxo
Version:        1.7.5
Release:        1%{?dist}
Summary:        A Library for Generating Text, XML, JSON, and HTML Output
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/Juniper/libxo
Source0:        https://github.com/Juniper/libxo/releases/download/%{version}/libxo-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
The libxo library allows an application to generate text, XML, JSON, and HTML 
output using a common set of function calls. The application decides at run 
time which output style should be produced. The application calls a function
"xo_emit" to product output that is described in a format string.
A "field descriptor" tells libxo what the field is and what it means.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-static
%make_build
%install
%make_install
find %{buildroot} -type f -name "*.la" | xargs rm -f
rm -f %{buildroot}%{_docdir}/libxo/Copyright
%{?ldconfig_scriptlets}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libxo-devel -f %{oreon_filedir}/libxo-devel.list

%changelog

%autochangelog
