%global source0_hash 75e586fbfda812fb26fbc2b05cf98e707f432705625004c9ff979f6d1f6657a0
Name:           repo
Version:        2.67
Release:        1%{?dist}
Summary:        Repository management tool built on top of git
License:        Apache-2.0
URL:            https://gerrit.googlesource.com/git-repo
Source0:        https://gerrit.googlesource.com/git-%{name}/+archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       git
Requires:       gnupg2
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-repo = %{version}-%{release}
# /oreon:deps
%description
Repo is a tool built on top of Git. Repo helps manage many Git repositories,
does the uploads to revision control systems, and automates parts of the
development workflow. Repo is not meant to replace Git, only to make it easier
to work with Git.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
install -Dpm0755 -t %{buildroot}%{_bindir} %{name}
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 man/%{name}*.1
install -Dpm0644 completion.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
%oreon_autofiles main

%check

%{py3_test_envvars} %{python3} -c 'import multiprocessing, pytest; multiprocessing.set_start_method("fork"); pytest.main()'
%files

%changelog

%autochangelog
