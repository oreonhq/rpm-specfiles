%global source0_hash fbd0f29738015d9613741932d189f0de706ef1f875cf51b04f9d23da7231701d
Name:           python-sure
Version:        2.0.1
Release:        1%{?dist}
Summary:        Idiomatic assertion toolkit with human-friendly failure messages
License:        GPL-3.0-or-later
URL:            https://github.com/gabrielfalcao/sure
Source0:        https://github.com/gabrielfalcao/sure/archive/refs/tags/2.0.1.tar.gz#/sure-2.0.1.tar.gz
Source1:        sure.1
Patch:          python3.10-workaround.patch
Patch:        https://github.com/gabrielfalcao/sure/pull/188.patch
Patch:          ast.patch
BuildArch:      noarch
%global common_description %{expand:
An idiomatic testing library for python with powerful and flexible assertions
created by Gabriel Falcão. Sure’s developer experience is inspired and modeled
after RSpec Expectations and should.js.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-sure = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-sure
Summary:        Idiomatic assertion toolkit with human-friendly failure messages
Obsoletes:      python-sure-doc < 2.0.1-9
%description -n python3-sure %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n sure-%{version}

# Do not generate a coverage report; this obviates the BR on pytest-cov
sed -r -i 's/[[:blank:]]--cov=[^[:blank:]]+//' setup.cfg

%build

%pyproject_wheel
%install
%pyproject_install
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 '%{SOURCE1}'
%oreon_autofiles python3-sure usr/lib/python3*/site-packages/sure* usr/lib64/python3*/site-packages/sure* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sure* usr/lib64/python3*/site-packages/sure* usr/bin/*

%check

%pytest --ignore=tests/test_old_api.py
%files
%files -n python3-sure -f %{oreon_filedir}/python3-sure.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.1-1
- Prepare for Oreon 11 (RP1)
