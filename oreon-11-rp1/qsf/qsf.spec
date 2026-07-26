%global source0_hash 1d3c1b8d7883307ba8c398b94472b701e949ec268a4de77f24729285cac3fc75

%bcond_without gdbm
%bcond_with sqlite
%bcond_with mysql

Name:           qsf
Version:        1.2.23
Release:        2%{?dist}
Summary:        Quick Spam Filter

License:        Artistic-2.0
URL:            https://ivarch.com/programs/qsf/
Source0:        https://ivarch.com/s/qsf-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%{?with_gdbm:BuildRequires: gdbm-devel}
%{?with_sqlite:BuildRequires: sqlite2-devel}
%{?with_mysql:BuildRequires: mariadb-connector-c-devel}

%description
Quick Spam Filter (QSF) is an Open Source email classification filter,
designed to be small, fast, and accurate, which works to classify
incoming email as either spam or non-spam.

To recognise spam, QSF strips the text out of the email (using MIME
decoding and HTML stripping) and then splits it into tokens (words,
word pairs, URLs, and so on). These tokens are then looked up in a
database and analysed using the Bayesian technique to see whether the
email should be classified as spam or not.

QSF is designed to be run by an MDA, such as procmail.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure \
%{!?with_gdbm:    --without-gdbm} \
%{!?with_sqlite:  --without-sqlite} \
%{!?with_mysql:   --without-mysql} \
;
%make_build

%check
make test

%install
%make_install
rm -rf %{buildroot}%{_docdir}

%files
%license docs/COPYING
%doc README.md docs/ACKNOWLEDGEMENTS.md docs/NEWS.md docs/postfix-howto
%{_bindir}/qsf
%{_mandir}/man1/qsf.1*

%changelog
%autochangelog
