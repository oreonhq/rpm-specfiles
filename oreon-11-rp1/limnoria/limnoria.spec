%global source0_hash 634bb1999fefde0cdb4089b2547d5cd059f690218cf8f215f325eaa31d235121

%global upstreamver 2026-01-16

Name:           limnoria
Version:        20260116
Release:        1%{?dist}
Summary:        A modified version of Supybot (an IRC bot) with enhancements and bug fixes

License:        BSD-3-Clause AND GPL-2.0-only AND GPL-2.0-or-later
#
# The bulk of the package is BSD-3-Clause.
# Parts of the Math plugin are GPL-2.0-only
# The Dict plugin is GPL-2.0-or-later
#
URL:            https://github.com/ProgVal/Limnoria
Source0:        %{url}/archive/master-%{upstreamver}.tar.gz

BuildArch:      noarch

# Provide the upper case version also to avoid confusion
Provides: Limnoria = %{version}-%{release}

#
# Obsolete the supybot-gribble package as this is a newer/maintained fork.
#
Obsoletes: supybot-gribble =< 0.83.4.1-18%{dist}
Provides: supybot-gribble = 0.83.4.1-19%{dist}

BuildRequires:  python3-devel
Requires:  python3-chardet
Requires:  python3-dateutil
Requires:  python3-gnupg
Requires:  python3-feedparser
Requires:  python3-sqlalchemy
Requires:  python3-pysocks
Requires:  python3-ecdsa

%description
Supybot is a robust (it doesn't crash), user friendly 
(it's easy to configure) and programmer friendly 
(plugins are extremely easy to write) Python IRC bot.
It aims to be an adequate replacement for most existing IRC bots.
It includes a very flexible and powerful ACL system for controlling 
access to commands, as well as more than 50 builtin plugins 
providing around 400 actual commands.

Limnoria is a project which continues development of Supybot 
(you can call it a fork) by fixing bugs and adding features 
(see the list of added features for more details).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Limnoria-master-%{upstreamver}
# remove stray python bits from debug plugin
sed -i 1"s|#!/usr/bin/python||" plugins/Debug/plugin.py

%generate_buildrequires
%pyproject_buildrequires

%build
# This should be set to the day of the release. 
# It's gets added as 'version' and is based on build time, not release time.
SOURCE_DATE_EPOCH=`date --date=%{version} +\%s`
export SOURCE_DATE_EPOCH
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files supybot

# TODO: get tests working
#check

%files -f %{pyproject_files}
%doc CONTRIBUTING.md README.md
%license LICENSE.md
%{_bindir}/supybot
%{_bindir}/supybot-adduser
%{_bindir}/supybot-botchk
%{_bindir}/supybot-plugin-create
%{_bindir}/supybot-plugin-doc
%{_bindir}/supybot-test
%{_bindir}/supybot-wizard
%{_bindir}/supybot-reset-password
%{_mandir}/man1/supybot-adduser.1.gz
%{_mandir}/man1/supybot-botchk.1.gz
%{_mandir}/man1/supybot-plugin-create.1.gz
%{_mandir}/man1/supybot-plugin-doc.1.gz
%{_mandir}/man1/supybot-test.1.gz
%{_mandir}/man1/supybot-wizard.1.gz
%{_mandir}/man1/supybot.1.gz
%{_mandir}/man1/supybot-reset-password.1.gz
%{_bindir}/limnoria
%{_bindir}/limnoria-adduser
%{_bindir}/limnoria-botchk
%{_bindir}/limnoria-plugin-create
%{_bindir}/limnoria-plugin-doc
%{_bindir}/limnoria-test
%{_bindir}/limnoria-wizard
%{_bindir}/limnoria-reset-password
%{_mandir}/man1/limnoria-adduser.1.gz
%{_mandir}/man1/limnoria-botchk.1.gz
%{_mandir}/man1/limnoria-plugin-create.1.gz
%{_mandir}/man1/limnoria-plugin-doc.1.gz
%{_mandir}/man1/limnoria-test.1.gz
%{_mandir}/man1/limnoria-wizard.1.gz
%{_mandir}/man1/limnoria.1.gz
%{_mandir}/man1/limnoria-reset-password.1.gz

%changelog
%autochangelog
