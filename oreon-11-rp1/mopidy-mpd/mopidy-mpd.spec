%global source0_hash d816666182ec4396fdbb6b5c367760257be9a3e2952ff84490d21613cd097f8e

Name:           mopidy-mpd
Version:        4.0.0~a4
Release:        1%{?dist}
Summary:        Mopidy extension for controlling Mopidy from MPD clients

License:        Apache-2.0
URL:            https://mopidy.com/ext/mpd/
Source0:        https://files.pythonhosted.org/packages/source/m/mopidy-mpd/mopidy_mpd-4.0.0a4.tar.gz
# package has been renamed from Mopidy-MPD to mopidy_mpd, pypi_source can't handle that.
%dnl Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-mock
BuildRequires:  tox
BuildRequires:  python3-tox-current-env
BuildRequires:  mopidy >= 4.0.0~a10
Requires:       mopidy >= 4.0.0~a10

%description
Frontend that provides a full MPD server implementation to make Mopidy
available from MPD clients.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n mopidy_mpd-4.0.0a4 -p1
#^TODO: revert to %%autosetup -n %%{name}-%%{version} -p1
rm -f setup.cfg # HACK: work around https://github.com/tox-dev/tox/issues/3602

%generate_buildrequires
%pyproject_buildrequires -p

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l mopidy_mpd

%check
%tox

%files -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
