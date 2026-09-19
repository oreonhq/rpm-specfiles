%global source0_hash 4b8e565846c74753b74d4a2f2986fbb9f6e38ad3d62420920194cc5f821ad366

%global commit 7e23085e7da80c8805fff54cc18e2705ac332074
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global debug_package %{nil}

Name:           gdalcpp
Version:        1.3.0
Release:        11.20210925git%{shortcommit}%{?dist}
Summary:        C++11 wrapper classes for GDAL/OGR

License:        BSL-1.0
URL:            https://github.com/joto/gdalcpp
Source0:        https://github.com/joto/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz

%description
These are some small wrapper classes for GDAL offering:

* classes with RAII instead of the arcane cleanup functions in stock GDAL
* works with GDAL 1 and 2
* allows you to write less boilerplate code

The classes are not very complete, they just have the code I needed for
various programs.

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}

%description    devel
These are some small wrapper classes for GDAL offering:

* classes with RAII instead of the arcane cleanup functions in stock GDAL
* works with GDAL 1 and 2
* allows you to write less boilerplate code

The classes are not very complete, they just have the code I needed for
various programs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{commit}

%build

%install
mkdir -p %{buildroot}%{_includedir}
cp -p *.hpp  %{buildroot}%{_includedir}

%files devel
%doc README.md
%license LICENSE.txt
%{_includedir}/*.hpp

%changelog
%autochangelog
