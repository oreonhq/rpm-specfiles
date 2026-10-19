%global source2_hash eec7eccb51a27ae633784d1b1ef42eb775130c782ea51a6c47fa7a901484d6db
%global source1_hash 0a7359b65aeb8492f35e4e61ad70c3d79bdaa79e599afcfab9e5fbb0b902d083
%global source0_hash 0a629a4d23df9f5fb22c2af90778c6da1176f3907b412405f8518a9fdf405f1d
Name:           conflict
Version:        20250930
Release:        1%{?dist}
Summary:        Check for conflicting binary names on path
License:        MIT
URL:            https://invisible-island.net/conflict/conflict.html
Source0:        https://invisible-island.net/archives/conflict/conflict-%{version}.tgz
Source1:        https://invisible-island.net/archives/conflict/conflict-%{version}.tgz.asc
Source2:        https://invisible-island.net/public/dickey@invisible-island.net-rsa3072.asc
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  groff
BuildRequires:  make
# /oreon:deps
%description
CONFLICT examines the user-specifiable list of programs, looking for instances
in the user's path which conflict (i.e., the name appears in more than one
point in the path).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{name}-%{version}

%build

%configure --disable-stripping
%make_build
%install
%make_install
%oreon_autofiles main

%check

bash run_test.sh
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
