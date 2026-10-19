%global source0_hash e7acf4ee95177cab09f6b8dc12eff42ec2c53b2ace536fda5a30838d825ccdb5
Name:               python-slackclient
Version:            3.39.0
Release:        1%{?dist}
Summary:        Slack Developer Kit for Python
License:            MIT
URL:                https://github.com/slackapi/python-slack-sdk
Source0:        https://github.com/slackapi/python-slack-sdk/archive/v%{version}/python-slack-sdk-%{version}.tar.gz
BuildArch:          noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-slackclient = %{version}-%{release}
# /oreon:deps
%description
%{summary}.

%package -n python3-slackclient
Summary:        Slack Developer Kit for Python
%py_provides python3-slack
%py_provides python3-slack-sdk
Provides: python3-slackclient+optional = %{version}-%{release}
Obsoletes: python3-slackclient+optional < 3.26.2-1
%description -n python3-slackclient
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n python-slack-sdk-%{version} -p1
# Remove prebuilt HTML documentation with bundled and precompiled JavaScript
rm -rf docs docs-v*

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-slackclient usr/lib/python3*/site-packages/slackclient* usr/lib64/python3*/site-packages/slackclient* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/slackclient* usr/lib64/python3*/site-packages/slackclient* usr/bin/*

%check

k="${k-}${k+ and }not test_start_raises_an_error_if_rtm_ws_url_is_not_returned"
%pytest -k "${k-}" \
    --ignore-glob='integration_tests/*' \
    --ignore-glob='*/test_amazon_s3.py' \
    --ignore-glob='*/socket_mode/test_interactions_*' \
    --ignore-glob='*/rtm/test_rtm_client*' \
    --ignore-glob='*test_async_sqlalchemy.py'
%files
%files -n python3-slackclient -f %{oreon_filedir}/python3-slackclient.list

%changelog

%autochangelog
