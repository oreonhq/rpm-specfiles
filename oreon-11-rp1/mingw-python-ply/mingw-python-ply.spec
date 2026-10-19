%global source0_hash 00c7c1aaa88358b9c765b6d3000c6eec0ba42abca5351b095321aef446081da3
%{?mingw_package_header}
%global pypi_name ply
Name:          mingw-python-%{pypi_name}
Summary:        MinGW Windows Python ply library
Version:       3.11
Release:        1%{?dist}
BuildArch:     noarch
License:       BSD
URL:           http://www.dabeaz.com/ply/
Source0:        http://www.dabeaz.com/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-python3-build
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-python3-build
# /oreon:deps
%description
MinGW Windows Python %{pypi_name} library.

%package -n mingw32-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name} library
%description -n mingw32-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name} library.

%package -n mingw64-python3-%{pypi_name}
Summary:       MinGW Windows Python3 %{pypi_name} library
%description -n mingw64-python3-%{pypi_name}
MinGW Windows Python3 %{pypi_name} library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

# extract license block from beginning of README.md
grep -B1000 "POSSIBILITY OF SUCH DAMAGE" README.md > LICENSE

%build

%mingw32_py3_build_wheel
%mingw64_py3_build_wheel
%install
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-python3-ply -f %{oreon_filedir}/mingw32-python3-ply.list
%files -n mingw64-python3-ply -f %{oreon_filedir}/mingw64-python3-ply.list

%changelog

%autochangelog
