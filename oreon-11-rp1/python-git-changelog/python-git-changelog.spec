%global source0_hash 1192a29a8ab7c8d7c371ead7866912ce5716ec8d6aefb8ca7b1a186fb97a1beb
%bcond check 0
Name:           python-git-changelog
Version:        2.9.7
Release:        1%{?dist}
Summary:        Automatic Changelog generator using Jinja2 templates
License:        ISC
URL:            https://github.com/pawamoy/git-changelog
Source0:        https://github.com/pawamoy/git-changelog/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
%if %{with check}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-git-changelog = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-git-changelog
Requires:       git-core
Summary:        Automatic Changelog generator using Jinja2 templates
# oreon:reqs
Requires:       python3dist(jinja2) >= 3.0
Requires:       python3dist(packaging) >= 26.0
Requires:       python3dist(platformdirs) >= 4.4
Requires:       python3dist(semver) >= 3.0
Requires:       python3dist(tomli) >= 2.0
Requires:       python3dist(typing-extensions) >= 4.9
# /oreon:reqs
%description -n python3-git-changelog

%prep

%autosetup -n git-changelog-%{version} -S git
sed -i 's/Jinja2>=[0-9]\+\.[0-9]\+/Jinja2/' pyproject.toml
sed -i 's/platformdirs>=[0-9]\+\.[0-9]\+/platformdirs/' pyproject.toml
git tag %{version}

%if %{with check}
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-git-changelog usr/lib/python3*/site-packages/git_changelog* usr/lib64/python3*/site-packages/git_changelog* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/git_changelog* usr/lib64/python3*/site-packages/git_changelog* usr/bin/*

%check

%pytest
%endif
%files
%files -n python3-git-changelog -f %{oreon_filedir}/python3-git-changelog.list

%changelog

%autochangelog
