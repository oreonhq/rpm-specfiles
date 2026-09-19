%global source0_hash f226bcff06d04623a8b196d5f1ee50e0fbc7744e08eafd55c7a49df3c8b4b67c

%global commit 3a7c84896f2dcdbd6fc13fb5df11af43b92ec850
%global shortcommit %{sub %{commit} 1 7}
%global commitdate 20240927

Name:           almalinux-git-utils
Version:        0.0.3^git%{commitdate}.%{shortcommit}
Release:        7%{?dist}
Summary:        Utilities for working with the AlmaLinux Git server

License:        GPL-3.0-or-later
URL:            https://git.almalinux.org/almalinux/almalinux-git-utils
Source0:        %{url}/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l almalinux

%check
%pytest -v

%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/alma_blob_upload
%{_bindir}/alma_get_sources

%changelog
%autochangelog
