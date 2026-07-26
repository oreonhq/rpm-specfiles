%global source0_hash eb14b7d00ec0eef33994a208ebff024aeef9a17b6897bece9d77241fddf0767f

# BSD 2-Clause License
#
# Apprise - Push Notification Library.
# Copyright (c) 2025, Chris Caron <lead2gold@gmail.com>
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
###################################################################
%if 0%{?_module_build}
%bcond_with tests
%else
# When bootstrapping Python, we cannot test this yet
%bcond_without tests
%endif

# Handling of new python building structure (for backwards compatiblity)
%global legacy_python_build 0
%if 0%{?fedora} && 0%{?fedora} <= 29
%global legacy_python_build 1
%endif
%if 0%{?rhel} && 0%{?rhel} <= 9
%global legacy_python_build 1
%endif

%global pypi_name apprise

# Handle rpmlint false positives
# - Prevent warnings:
#    en_US ntfy -> notify
#    en_US httpSMS -> HTTP
#
# rpmlint: ignore-spelling httpSMS ntfy

# - RHEL9 does not recognize: BSD-2-Clause which is correct
#
# rpmlint: ignore invalid-license

%global common_description %{expand: \
Apprise is a Python package that simplifies access to many popular \
notification services. It supports sending alerts to platforms such as: \
\
`46elks`, `AfricasTalking`, `Apprise API`, `APRS`, `AWS SES`, `AWS SNS`, \
`Bark`, `BlueSky`, `Brevo`, `Burst SMS`, `BulkSMS`, `BulkVS`, `Chanify`, \
`Clickatell`, `ClickSend`, `DAPNET`, `DingTalk`, `Discord`, \
`Dot. (Quote/0)`, `E-Mail`, `Emby`, `FCM`, `Feishu`, `Flock`, \
`Free Mobile`, `Google Chat`, `Gotify`, `Growl`, `Guilded`, \
`Home Assistant`, `httpSMS`, `IFTTT`, `Join`, `Kavenegar`, `KODI`, \
`Kumulos`, `LaMetric`, `Lark`, `Line`, `MacOSX`, `Mailgun`, \
`Mastodon`, `Mattermost`, `Matrix`, `MessageBird`, `Microsoft Windows`, \
`Microsoft Teams`, `Misskey`, `MQTT`, `MSG91`, `MyAndroid`, `Nexmo`, \
`Nextcloud`, `NextcloudTalk`, `Notica`, `NotificationAPI`, `Notifiarr`, \
`Notifico`, `ntfy`, `Office365`, `OneSignal`, `Opsgenie`, `PagerDuty`, \
`PagerTree`, `ParsePlatform`, `Plivo`, `PopcornNotify`, `Prowl`, `Pushalot`, \
`PushBullet`, `Pushjet`, `PushMe`, `Pushover`, `Pushplus`, `PushSafer`, \
`Pushy`, `PushDeer`, `QQ Push`, `Revolt`, `Reddit`, `Resend`, \
`Rocket.Chat`, `RSyslog`, `SendGrid`, `SendPulse`, `ServerChan`, `Seven`, \
`SFR`, `Signal`, `SIGNL4`, `SimplePush`, `Sinch`, `Slack`, `SMPP`, \
`SMSEagle`, `SMS Manager`, `SMTP2Go`, `SparkPost`, `Splunk`, `Spike`, \
`Spug Push`, `Super Toasty`, `Streamlabs`, `Stride`, `Synology Chat`, \
`Syslog`, `Techulus Push`, `Telegram`, `Threema Gateway`, `Twilio`, \
`Twitter`, `Twist`, `Vapid`, `VictorOps`, `Voipms`, `Vonage`, `WebPush`, \
`WeCom Bot`, `WhatsApp`, `Webex Teams`, `Workflows`, `WxPusher`, and `XBMC`.}

Name:           python-%{pypi_name}
Version:        1.9.7
Release:        2%{?dist}
Summary:        A simple wrapper to many popular notification services used today
License:        BSD-2-Clause
URL:            https://github.com/caronc/%{pypi_name}
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description %{common_description}

%package -n %{pypi_name}
Summary: Notify messaging platforms from the command line

Obsoletes: %{pypi_name} < %{version}-%{release}
Provides: %{pypi_name} = %{version}-%{release}

Requires: python3dist(click) >= 5.0
Requires: python%{python3_pkgversion}-%{pypi_name} = %{version}-%{release}

%description -n %{pypi_name}
An accompanied CLI tool that can be used as part of Apprise
to issue notifications from the command line to you favorite
services.

%package -n python%{python3_pkgversion}-%{pypi_name}
Summary: A simple wrapper to many popular notification services used today

Obsoletes: python%{python3_pkgversion}-%{pypi_name} < %{version}-%{release}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

BuildRequires: gettext
BuildRequires: python%{python3_pkgversion}-devel

%if %{legacy_python_build}
BuildRequires: python3dist(setuptools)
%endif

BuildRequires: python3dist(wheel)
BuildRequires: python3dist(requests)
BuildRequires: python3dist(requests-oauthlib)
BuildRequires: python3dist(click) >= 5.0
BuildRequires: python3dist(markdown)
BuildRequires: python3dist(pyyaml)
BuildRequires: python3dist(babel)
BuildRequires: python3dist(cryptography)
BuildRequires: python3dist(certifi)
BuildRequires: python3dist(tox)

%if %{with tests}
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(pytest-mock)
%endif

Requires: python3dist(requests)
Requires: python3dist(requests-oauthlib)
Requires: python3dist(markdown)
Requires: python3dist(cryptography)
Requires: python3dist(certifi)
Requires: python3dist(pyyaml)

Recommends: python3dist(paho-mqtt)

%if 0%{?legacy_python_build} == 0
# Logic for non-RHEL ≤ 9 systems
%generate_buildrequires
%pyproject_buildrequires
%endif

%description -n python%{python3_pkgversion}-%{pypi_name} %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%build
%if %{legacy_python_build}
# backwards compatible
%py3_build
%else
%pyproject_wheel
%endif

%install
%if %{legacy_python_build}
# backwards compatible
%py3_install
# Compile gettext catalogues from SOURCE into the INSTALLED tree
pushd %{_builddir}/%{pypi_name}-%{version}
for po in apprise/i18n/*/LC_MESSAGES/apprise.po; do
    [ -f "$po" ] || continue
    langdir="$(dirname "${po#apprise/i18n/}")"
    outdir="%{buildroot}%{python3_sitelib}/%{pypi_name}/i18n/${langdir}"
    install -d "$outdir"
    msgfmt -o "${outdir}/apprise.mo" "$po"
done
%else
%pyproject_install
%pyproject_save_files apprise

# Compile gettext catalogues into the installed tree
pushd %{buildroot}%{python3_sitelib}/apprise/i18n
for po in */LC_MESSAGES/apprise.po; do
    [ -f "$po" ] || continue
    msgfmt -o "${po%.po}.mo" "$po"
done
%endif

popd

%{__install} -p -D -T -m 0644 packaging/man/%{pypi_name}.1 \
   %{buildroot}%{_mandir}/man1/%{pypi_name}.1

%if %{with tests}
%check
%if %{legacy_python_build}
# backwards compatible
LANG=C.UTF-8 PYTHONPATH=%{buildroot}%{python3_sitelib}:%{_builddir}/%{name}-%{version} py.test-%{python3_version}
%else
%pytest
%endif
%endif

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc SECURITY.md README.md ACKNOWLEDGEMENTS.md CONTRIBUTING.md
%{python3_sitelib}/%{pypi_name}/
# Exclude i18n as it is handled below with the lang(spoken) tag below
%exclude %{python3_sitelib}/%{pypi_name}/cli.*
%exclude %{python3_sitelib}/%{pypi_name}/__pycache__/cli*.py?

%if %{legacy_python_build}
# Handle egg-info vs. dist-info based on build backend
%{python3_sitelib}/apprise-*.egg-info
# Legacy: include all compiled locales that we produced under the package tree
%lang(en) %{python3_sitelib}/%{pypi_name}/i18n/en/LC_MESSAGES/apprise.mo
%else
# Handle egg-info vs. dist-info based on build backend
%{python3_sitelib}/apprise-*.dist-info/
# Localised Files
%exclude %{python3_sitelib}/%{pypi_name}/i18n/
%lang(en) %{python3_sitelib}/%{pypi_name}/i18n/en/LC_MESSAGES/apprise.mo
%endif

%files -n %{pypi_name}
%{_bindir}/%{pypi_name}
%{_mandir}/man1/%{pypi_name}.1*
%{python3_sitelib}/%{pypi_name}/cli.py
%{python3_sitelib}/%{pypi_name}/__pycache__/cli*.py?

%changelog
%autochangelog
