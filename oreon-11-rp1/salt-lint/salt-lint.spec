%global source0_hash 1dee5bb2872b435169193ebae63620b365d1715f28db6e89f3bf61fffa901458

Name:           salt-lint
Version:        0.9.2
Release:        12%{?dist}
Summary:        Salt State file (SLS) lint tool

License:        MIT
URL:            https://github.com/warpnet/salt-lint
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# This is a downstream only patch persuant to
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch0:         00-remove-linter-deps.patch

BuildRequires:  python3-devel
BuildArch:      noarch

%description
salt-lint checks Salt State files (SLS) for best practices and behavior that
could potentially be improved.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files saltlint
install -Dpm 0644 docs/man/salt-lint.1 %{buildroot}%{_mandir}/man1/salt-lint.1

%check
%tox

%files -f %{pyproject_files}
%license LICENSE*
%doc README.*
%{_bindir}/%{name}
%{_mandir}/man1/salt-lint.1*

%changelog
%autochangelog
