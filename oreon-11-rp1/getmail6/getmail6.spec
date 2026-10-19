%global source0_hash 96c16f685e7c21cce8f2312a2781fae5dc2f11182bd1eeb8b9350cf82390db68
Name:           getmail6
Version:        6.20.1
Release:        1%{?dist}
Summary:        A mail retrieval, sorting, and delivering system
License:        GPL-2.0-only and Apache-2.0
URL:            https://www.getmail6.org/
Source0:        https://files.pythonhosted.org/packages/source/g/getmail6/getmail6-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-getmail6 = %{version}-%{release}
# /oreon:deps
%description
A mail retriever with support for POP3, POP3-over-SSL, IMAP4,
IMAP4-over-SSL, and SDPS mail accounts. It supports normal single-user
mail accounts and multidrop (domain) mailboxes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir getmail6-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%check

%pyproject_check_import
%pytest
%files

%changelog

%autochangelog
