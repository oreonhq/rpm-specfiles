%global source0_hash 9a3f912b4b69a316132f3b72e15023ffcb7adef2cf2da7a467cb341055838328

Name:           python-zstarfile
Version:        0.3.0
Release:        1%{?dist}
Summary:        Tarfile extension with additional compression algorithms and PEP 706 by default

License:        MIT
URL:            https://sr.ht/~gotmax23/zstarfile
%global furl    https://git.sr.ht/~gotmax23/zstarfile
Source0:        %{furl}/refs/download/v%{version}/zstarfile-%{version}.tar.gz
Source1:        %{furl}/refs/download/v%{version}/zstarfile-%{version}.tar.gz.asc
Source2:        https://meta.sr.ht/~gotmax23.pgp

BuildArch:      noarch

BuildRequires:  gnupg2
BuildRequires:  gpgverify
BuildRequires:  python3-devel

%global _description %{expand:
zstarfile is a tarfile extension with additional compression algorithms and
PEP 706 by default.}

%description %_description

%package -n python3-zstarfile
Summary:        %{summary}

%description -n python3-zstarfile %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%gpgverify -d0 -s1 -k2
%autosetup -p1 -n zstarfile-%{version}

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files zstarfile

%check
%pytest

%files -n python3-zstarfile -f %{pyproject_files}
%doc README.md
%license LICENSES/*

%changelog
%autochangelog
