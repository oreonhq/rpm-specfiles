%global source0_hash ea09b68f6a5421b0bd50e98e24d49a0a33bd54a5f59d0f1be1f6f3f05b8c6087
Name:           rss2email
Version:        3.14
Release:        17%{?dist}
Summary:        Deliver news from RSS feeds to your SMTP server as text or HTML mail
License:        GPL-2.0-or-later OR GPL-3.0-or-later
URL:            https://github.com/%{name}/%{name}
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz
Source1:        r2e-migrate
Source2:        r2e-migrate.1
Source3:        README.migrate
Patch1:         rss2email-3.14-remove-special-bytes.patch
Patch2:         rss2email-3.14-fix-tests-pr-279.patch
BuildArch:      noarch
Recommends:     python3-beautifulsoup4
Recommends:     esmtp
Requires:       python3-pyxdg
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry) >= 0.12
Requires:       python3-rss2email = %{version}-%{release}
# /oreon:deps
%description
%{name} lets you subscribe to a list of XML news feeds (RSS or Atom). It can
parse them regularly with the help of cron and send new items to you by email.

An HTML mail will be send in the default configuration to the local SMTP server.
See the manual page r2e for details on how to set up %{name}.

%package zsh-completion
Summary:        zsh-completion files for rss2email
BuildArch:      noarch
Supplements:    (rss2email and zsh)
Requires:       zsh
Requires:       rss2email
%description zsh-completion
This package provides %{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

cp -p %{SOURCE3} .

%build

%pyproject_wheel
%install
%pyproject_install
install -D -m 644 -p completion/r2e.zsh %{buildroot}%{_datadir}/zsh/functions/Completion/Unix/_r2e
install -D -m 644 -p r2e.1 %{buildroot}%{_mandir}/man1/r2e.1
install -D -m 755 -p %{SOURCE1} %{buildroot}%{_bindir}/r2e-migrate
install -D -m 644 -p %{SOURCE2} %{buildroot}%{_mandir}/man1/r2e-migrate.1
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pyproject_check_import
PATH="${PATH}:%{buildroot}%{_bindir}" PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} ./test/test.py
%files
%files -n rss2email-zsh-completion -f %{oreon_filedir}/rss2email-zsh-completion.list

%changelog

%autochangelog
