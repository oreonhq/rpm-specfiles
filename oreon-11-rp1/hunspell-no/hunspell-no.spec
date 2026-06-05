%global source0_hash none

%if 0%{?rhel} && 0%{?rhel} > 9
%bcond_with mythes
%else
%bcond_without mythes
%endif

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9 || (0%{?oreon} >= 11)
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-no
Summary: Norwegian hunspell dictionaries
Epoch: 1
Version: 25.2.3
Release: 2%{?dist}

Source0:        https://deb.debian.org/debian/pool/main/libr/libreoffice-dictionaries/libreoffice-dictionaries_25.2.3.orig.tar.xz#/libreoffice-dictionaries-25.2.3.tar.xz
URL: https://cgit.freedesktop.org/libreoffice/dictionaries/tree/no
License: GPL-1.0-or-later
BuildArch: noarch

Patch1:  rhbz959989.badsfxrules.patch

%description
Norwegian hunspell dictionaries.

%package -n hunspell-nb
Summary: Bokmaal hunspell dictionaries
Requires: hunspell
Supplements: (hunspell and langpacks-nb)

%description -n hunspell-nb
Bokmaal hunspell dictionaries.

%package -n hunspell-nn
Summary: Nynorsk hunspell dictionaries
Requires: hunspell
Supplements: (hunspell and langpacks-nn)

%description -n hunspell-nn
Nynorsk hunspell dictionaries.

%package -n hyphen-nb
Summary: Bokmaal hyphenation rules
Requires: hyphen
Supplements: (hyphen and langpacks-nb)

%description -n hyphen-nb
Bokmaal hyphenation rules.

%package -n hyphen-nn
Summary: Nynorsk hyphenation rules
Requires: hyphen
Supplements: (hyphen and langpacks-nn)

%description -n hyphen-nn
Nynorsk hyphenation rules

%if %{with mythes}
%package -n mythes-nb
Summary: Bokmaal thesaurus
Requires: mythes
Supplements: (mythes and langpacks-nb)

%description -n mythes-nb
Bokmaal thesaurus.

%package -n mythes-nn
Summary: Nynorsk thesaurus
Requires: mythes
Supplements: (mythes and langpacks-nn)

%description -n mythes-nn
Nynorsk thesaurus.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n libreoffice-25.2.3.2
cp dictionaries/no/nn_NO.aff .
%patch 1 -p0

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{dict_dirname}
install -pm 0644 dictionaries/no/nb_NO.aff dictionaries/no/nb_NO.dic %{buildroot}%{_datadir}/%{dict_dirname}/
install -pm 0644 nn_NO.aff dictionaries/no/nn_NO.dic %{buildroot}%{_datadir}/%{dict_dirname}/
mkdir -p %{buildroot}%{_datadir}/hyphen
install -pm 0644 dictionaries/no/hyph_nb_NO.dic dictionaries/no/hyph_nn_NO.dic %{buildroot}%{_datadir}/hyphen/
%if %{with mythes}
mkdir -p %{buildroot}%{_datadir}/mythes
install -pm 0644 dictionaries/no/th_nb_NO_v2.dat dictionaries/no/th_nn_NO_v2.dat %{buildroot}%{_datadir}/mythes/
%endif

%files -n hunspell-nb
%{_datadir}/%{dict_dirname}/nb_NO.*

%files -n hunspell-nn
%{_datadir}/%{dict_dirname}/nn_NO.*

%files -n hyphen-nb
%doc dictionaries/no/README_hyph_NO.txt
%{_datadir}/hyphen/hyph_nb_NO.*

%files -n hyphen-nn
%doc dictionaries/no/README_hyph_NO.txt
%{_datadir}/hyphen/hyph_nn_NO.*

%if %{with mythes}
%files -n mythes-nb
%{_datadir}/mythes/th_nb_NO_v2.dat

%files -n mythes-nn
%{_datadir}/mythes/th_nn_NO_v2.dat
%endif

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.2.3-2
- Import
