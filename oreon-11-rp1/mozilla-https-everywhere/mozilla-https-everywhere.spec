%global source0_hash none

%global moz_extensions %{_datadir}/mozilla/extensions

%global firefox_app_id \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}
%global src_ext_id https-everywhere-eff@eff.org
%global firefox_inst_dir %{moz_extensions}/%{firefox_app_id}

%global seamonkey_app_id \{92650c4d-4b8e-4d2a-b7eb-24ecf4f6b63a}
%global seamonkey_inst_dir %{moz_extensions}/%{seamonkey_app_id}

Name:           mozilla-https-everywhere
Version:        2022.5.11
Release:        10%{?dist}
Summary:        HTTPS enforcement extension for Mozilla Firefox

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://eff.org/https-everywhere
# A git repo is available at https://github.com/EFForg/https-everywhere
Source0:        https://www.eff.org/files/https-everywhere-%{version}-eff.xpi
Source1:        mozilla-https-everywhere.metainfo.xml
Source2:        https://www.eff.org/files/https-everywhere-5.2.21-eff.xpi

Requires:       mozilla-filesystem
# GNOME Software Center not present on EL < 7
%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires:  libappstream-glib
%endif
BuildArch:      noarch

%description
HTTPS Everywhere is a Firefox extension produced as a collaboration between
The Tor Project and the Electronic Frontier Foundation. It encrypts your
communications with a number of major websites.

Many sites on the web offer some limited support for encryption over HTTPS,
but make it difficult to use. For instance, they may default to unencrypted
HTTP, or fill encrypted pages with links that go back to the unencrypted site.

The HTTPS Everywhere extension fixes these problems by rewriting all requests
to these sites to HTTPS.

The Fedora RPM package includes the legacy XUL version, no longer updated,
for SeaMonkey users.

%prep
%setup -q -c

%build

%install
# Install WebExtensions (supported) version to Firefox directory
install -Dpm644 %{SOURCE0} %{buildroot}%{firefox_inst_dir}/%{src_ext_id}.xpi

# Install XUL version to SeaMonkey directory
mkdir -p %{buildroot}%{seamonkey_inst_dir}
install -Dpm644 %{SOURCE2} %{buildroot}%{seamonkey_inst_dir}/%{src_ext_id}.xpi

# install MetaInfo file for firefox
%if 0%{?fedora} || 0%{?rhel} >= 7
appstream-util validate-relax %{SOURCE1}
DESTDIR=%{buildroot} appstream-util install %{SOURCE1}
%endif

%files
%{firefox_inst_dir}/%{src_ext_id}.xpi
%{seamonkey_inst_dir}/%{src_ext_id}.xpi
# GNOME Software Center metadata
%if 0%{?fedora} || 0%{?rhel} >= 7
%{_datadir}/appdata/%{name}.metainfo.xml
%endif

%changelog
%autochangelog
