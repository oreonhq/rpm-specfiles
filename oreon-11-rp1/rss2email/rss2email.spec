%global source0_hash ea09b68f6a5421b0bd50e98e24d49a0a33bd54a5f59d0f1be1f6f3f05b8c6087

Name:           rss2email
Version:        3.14
Release:        17%{?dist}
Summary:        Deliver news from RSS feeds to your SMTP server as text or HTML mail

# Automatically converted from old format: GPLv2+ or GPLv3+ - review is highly recommended.
License:        GPL-2.0-or-later OR GPL-3.0-or-later
URL:            https://github.com/%{name}/%{name}
Source0:        %{url}/archive/v%{version}.tar.gz
# Migration tool (rss2email 2.x to rss2email 3.x) from https://github.com/emillon/rss2email-debian
Source1:        r2e-migrate
Source2:        r2e-migrate.1
Source3:        README.migrate
Patch1:         rss2email-3.14-remove-special-bytes.patch
Patch2:         rss2email-3.14-fix-tests-pr-279.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-feedparser >= 6.0.5
BuildRequires:  python3-html2text >= 2018.1.9
BuildRequires:  python3-beautifulsoup4
Recommends:     python3-beautifulsoup4
Recommends:     esmtp
# r2e-migrate
Requires:       python3-pyxdg

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

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L %{name}

install -D -m 644 -p completion/r2e.zsh %{buildroot}%{_datadir}/zsh/functions/Completion/Unix/_r2e

install -D -m 644 -p r2e.1 %{buildroot}%{_mandir}/man1/r2e.1

install -D -m 755 -p %{SOURCE1} %{buildroot}%{_bindir}/r2e-migrate
install -D -m 644 -p %{SOURCE2} %{buildroot}%{_mandir}/man1/r2e-migrate.1

%check
%pyproject_check_import

PATH="${PATH}:%{buildroot}%{_bindir}" PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} ./test/test.py

%files -f %{pyproject_files}
%license COPYING
%doc AUTHORS CHANGELOG README.rst README.migrate
%{_bindir}/r2e
%{_bindir}/r2e-migrate
%{_mandir}/man1/r2e.1*
%{_mandir}/man1/r2e-migrate.1*

%files zsh-completion
%{_datadir}/zsh/functions/Completion/Unix/_r2e

%changelog
%autochangelog
