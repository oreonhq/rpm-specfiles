%global source0_hash 16058bd4d31271e351719073c6758906538ec74ac6b25f8fe65d08182469a3bb
Summary:        Dictionary of English words for the /usr/share/dict directory
Name: words
Version: 3.0
Release:        1%{?dist}
License: LicenseRef-Fedora-Public-Domain
URL: https://en.wikipedia.org/wiki/Moby_Project
Source0:        https://web.archive.org/web/20060527013227/http://www.dcs.shef.ac.uk/research/ilash/Moby/mwords.tar.Z
BuildArch: noarch
Patch0: words-3.0-typos.patch
Patch1: words-3.0-presidents.patch
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  grep
# /oreon:deps
%description
The words file is a dictionary of English words for the
/usr/share/dict directory. Some programs use this database of
words to check spelling. Password checkers use it to look for bad
passwords.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir mwords
%oreon_prep
%build

dos2unix -o *; chmod a+r *
cat [1-9]*.??? | grep -E --invert-match "'s$" | grep -E "^[[:alnum:]'&!,./-]+$" | sort --ignore-case --dictionary-order | uniq > moby
cat <<EOF >license.txt
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
EOF
%install
install -D -m644 moby $RPM_BUILD_ROOT%{_datadir}/dict/linux.words
ln -sf linux.words $RPM_BUILD_ROOT%{_datadir}/dict/words
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
