%global source0_hash 0e7b7094a02550dd80b7243bcffc3671550b0f1d8ba625e4dff52517827d5d23

# this is a header-only library with architecture-dependent .pc file
%global debug_package %{nil}

Name:           tllist
Version:        1.1.0
Release:        8%{?dist}
Summary:        C header file only implementation of a typed linked list

License:        MIT
URL:            https://codeberg.org/dnkl/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson >= 0.54

%global  _description %{expand:
%{name} is a C header-only implementation of a linked list that uses
pre-processor macros to implement dynamic types, where the data carrier
is typed to whatever you want; both primitive data types are supported
as well as aggregated ones such as structs, enums and unions.}

%description    %{_description}

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}

%description    devel %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}

%build
%meson
%meson_build

%install
%meson_install
# license will be installed to correct location with rpm macros
rm -f %{buildroot}%{_docdir}/%{name}/LICENSE

%check
%meson_test

%files devel
%license LICENSE
%{_includedir}/%{name}.h
%{_libdir}/pkgconfig/%{name}.pc
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/README.md

%changelog
%autochangelog
