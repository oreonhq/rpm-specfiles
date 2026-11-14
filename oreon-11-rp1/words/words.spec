# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 16058bd4d31271e351719073c6758906538ec74ac6b25f8fe65d08182469a3bb

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Summary:        Dictionary of English words for the /usr/share/dict directory
Name:           words
Version:        3.0
Release:        1%{?dist}
License:        LicenseRef-Public-Domain
URL:            https://en.wikipedia.org/wiki/Moby_Project
Source0:        https://web.archive.org/web/20060527013227/http://www.dcs.shef.ac.uk/research/ilash/Moby/mwords.tar.Z
Patch0:         words-3.0-typos.patch
Patch1:         words-3.0-presidents.patch

BuildArch:      noarch

BuildRequires:  oreon-rpm-macros
BuildRequires:  grep
BuildRequires:  sed
BuildRequires:  findutils
BuildRequires:  coreutils

%description
The words file is a dictionary of English words for the
/usr/share/dict directory. Some programs use this database of
words to check spelling. Password checkers use it to look for bad
passwords.

%prep
%oreon_sha256
%autosetup -p1 -n mwords

%build
find . -maxdepth 1 -type f -exec sed -i 's/\r$//' {} +
chmod a+r *
cat [1-9]*.??? | grep -E --invert-match "'s$" | grep -E "^[[:alnum:]'&!,./-]+$" | sort --ignore-case --dictionary-order | uniq > moby

cat <<'LIC' >license.txt
***
    The license in the readme.txt file is original and DEPRECATED
    license of The Moby lexicon project.
***

On June 1, 1996 Grady Ward announced that the fruits of
the Moby project were being placed in the public domain:

The Moby lexicon project is complete and has
been place into the public domain. Use, sell,
rework, excerpt and use in any way on any platform.

Placing this material on internal or public servers is
also encouraged. The compiler is not aware of any
export restrictions so freely distribute world-wide.

You can verify the public domain status by contacting

Grady Ward
3449 Martha Ct.
Arcata, CA  95521-4884

daedal@myrealbox.com
LIC

%install
install -Dpm0644 moby %{buildroot}%{_datadir}/dict/linux.words
ln -sf linux.words %{buildroot}%{_datadir}/dict/words

%check
test -s moby
grep -qx Barack moby
grep -qx Obama moby

%files
%license license.txt
%doc readme.txt
%{_datadir}/dict/linux.words
%{_datadir}/dict/words

%changelog
%autochangelog
