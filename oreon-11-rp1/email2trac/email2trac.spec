%global source0_hash 78056ded9e5df4bbb9690dafe2075be41d067d4aeeaee7eabedece2b6e0e87b6

# This spec file was derived from the upstream .spec file written by
# Jon Topper <jon at topper dot me dot uk>

# for now, Python3 support is on the main branch only
%global commit 0747a5a167ab236e86dcbd72f566457c4c28e29a
%global snapdate 20240910

Name:           email2trac
Version:        2.14.0^%{snapdate}git%{sub %{commit} 1 7}
Release:        4%{?dist}
Summary:        Utilities for converting emails to trac tickets
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://gitlab.com/surfsara/email2trac
# Source0:        https://mirror.ia.surf.nl/opensource/email2trac/email2trac-%%{version}.tar.gz
Source0:        https://gitlab.com/surfsara/email2trac/-/archive/%{commit}/email2trac-%{commit}.tar.gz
BuildRequires:  python3-devel
BuildRequires:  gcc
BuildRequires:  make
Requires:       trac
Patch0:         email2trac-2.8.4-installperms.patch

%description
This is a release of the SARA package email2trac that contains
utilities that we use to convert emails to trac tickets. The initial
setup was made by Daniel Lundin from Edgewall Software. SARA has
extend the initial setup, with the following extensions:

 * HTML message conversion
 * Attachments
 * Tickets can be updated via email
 * Use command-line options
 * Configuration file to control the behavior.
 * Unicode support
 * SPAM detection
 * Workflow support
 * FullBlogPlugin support
 * DiscussionPlugin support

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n email2trac-%{commit}

%build
export PYTHON=%{__python3}
%configure --with-trac_user=apache
%make_build

%install
make install DESTDIR=%{buildroot}

%files
%doc AUTHORS ChangeLog NOTICE README.md
%license LICENSE
%{_bindir}/delete_spam
%{_bindir}/email2trac
%{_bindir}/run_email2trac
%config(noreplace) %{_sysconfdir}/email2trac.conf

%changelog
%autochangelog
