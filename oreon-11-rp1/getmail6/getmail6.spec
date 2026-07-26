%global source0_hash 48e8f61d5c40739339940806e052077262db0e28e207c2e5adfb0af9c3110e8d

Name:           getmail6
Version:        6.19.10
Release:        %autorelease
Summary:        A mail retrieval, sorting, and delivering system
License:        GPL-2.0-only and Apache-2.0
URL:            https://www.getmail6.org/
Source:         %{pypi_source getmail6}

BuildArch:      noarch
BuildRequires:  python3-devel

# check
BuildRequires: python3-pytest

%description
A mail retriever with support for POP3, POP3-over-SSL, IMAP4,
IMAP4-over-SSL, and SDPS mail accounts. It supports normal single-user
mail accounts and multidrop (domain) mailboxes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n getmail6-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files 'getmailcore' +auto

%check
%pyproject_check_import
%pytest

%files -f %{pyproject_files}
%license docs/COPYING
%dir /usr/share/doc/getmail

%changelog
%autochangelog
