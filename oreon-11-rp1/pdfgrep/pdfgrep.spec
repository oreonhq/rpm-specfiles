%global source0_hash 0661e531e4c0ef097959aa1c9773796585db39c72c84a02ff87d2c3637c620cb

Summary:        Tool to search text in PDF files
Name:           pdfgrep
Version:        2.2.0
Release:        9%{?dist}

License:        GPL-2.0-or-later
URL:            https://pdfgrep.org/
Source0:        https://pdfgrep.org/download/%{name}-%{version}.tar.gz
Source1:        https://pdfgrep.org/download/%{name}-%{version}.tar.gz.asc
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/432FC753112F26D9EB48DDC1A17CF2CA697BEAF2

Patch:          pdfgrep-2.2.0-disallow-ligatures.patch

BuildRequires:  make
BuildRequires:  gnupg2
BuildRequires:  gcc-c++
BuildRequires:  poppler-cpp-devel >= 0.36.0
BuildRequires:  libgcrypt-devel >= 1.0.0
BuildRequires:  pcre2-devel
BuildRequires:  asciidoc
%if 0%{?fedora}
# Tests: runtest(1), pdflatex(1) with parskip.sty
BuildRequires:  dejagnu
BuildRequires:  texlive-latex
BuildRequires:  tex(parskip.sty)
# RHEL requires expl3.sty and pdftex.map explicitly
%if 0%{?rhel} && 0%{?rhel} < 10
BuildRequires:  tex(expl3.sty)
BuildRequires:  tex(pdftex.map)
%endif
%endif

%description
Pdfgrep is a tool, that works similar to grep, to search text in PDF files.
It tries to be compatible with GNU grep, thus many of the favorite GNU grep
options are supported. Pdfgrep can search many PDFs at once, even recursively
in directories. It supports regular expressions (POSIX and PCRE), provides
colored output and finally also support for password protected PDF files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

# /usr/share/texlive/texmf-dist/scripts/texlive/mktexlsr is run too early in dnf
# transaction on RHEL 8 and 9, thus pdflatex(1) is unusable - thanks Red Hat ;-(
%if 0%{?fedora}
# Tests are broken on s390x, see https://gitlab.com/pdfgrep/pdfgrep/-/issues/70
%ifnarch s390x
%check
make check
%endif
%endif

%files
%license COPYING
%doc AUTHORS NEWS.md README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/%{name}
%dir %{_datadir}/zsh/
%dir %{_datadir}/zsh/site-functions/
%{_datadir}/zsh/site-functions/_%{name}

%changelog
%autochangelog
