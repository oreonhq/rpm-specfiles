%if 0%{?rhel} && 0%{?rhel} > 9
%bcond_with mythes
%else
%bcond_without mythes
%endif

%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell 
%else
%global dict_dirname myspell
%endif

Name: hunspell-no
Summary: Norwegian hunspell dictionaries
Epoch: 1
Version: 2.2
Release: 2%{?dist}

Source: https://alioth-archive.debian.org/releases/spell-norwegian/spell-norwegian/%{version}/no_NO-pack2-%{version}.zip
URL: https://alioth-archive.debian.org/releases/spell-norwegian/spell-norwegian/
License: GPL-1.0-or-later
BuildArch: noarch

Patch1:  rhbz959989.badsfxrules.patch
# oreon url source checksums begin
%global source0_sha256 ab10c668f050eef16bb717c09f52eccf0887f248eb3738d255e169d72171d2fb
%global source0_file no_NO-pack2-2.2.zip
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/no_NO-pack2-2.2.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "ab10c668f050eef16bb717c09f52eccf0887f248eb3738d255e169d72171d2fb" || { echo "oreon: Source0 SHA256 mismatch for no_NO-pack2-2.2.zip" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -c
unzip -q nb_NO.zip
unzip -q nn_NO.zip
unzip -q hyph_nb_NO.zip
unzip -q hyph_nn_NO.zip
unzip -q th_nb_NO_v2.zip
unzip -q th_nn_NO_v2.zip
%patch -P 1 -b .rhbz959989

%build
for i in README_nb_NO.txt README_nn_NO.txt README_hyph_nb_NO.txt \
  README_hyph_nn_NO.txt README_th_nb_NO_v2.txt README_th_nn_NO_v2.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p nn_NO.aff nn_NO.dic nb_NO.aff nb_NO.dic $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_nn_NO.dic hyph_nb_NO.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen
%if %{with mythes}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_nb_NO_v2.dat th_nb_NO_v2.idx th_nn_NO_v2.dat th_nn_NO_v2.idx $RPM_BUILD_ROOT/%{_datadir}/mythes
%endif

%files -n hunspell-nb
%doc README_nb_NO.txt
%{_datadir}/%{dict_dirname}/nb_NO.*

%files -n hunspell-nn
%doc README_nn_NO.txt
%{_datadir}/%{dict_dirname}/nn_NO.*

%files -n hyphen-nb
%doc README_hyph_nb_NO.txt
%{_datadir}/hyphen/hyph_nb_NO.*

%files -n hyphen-nn
%doc README_hyph_nn_NO.txt
%{_datadir}/hyphen/hyph_nn_NO.*

%if %{with mythes}
%files -n mythes-nb
%doc README_th_nb_NO_v2.txt
%{_datadir}/mythes/th_nb_NO_v2.*

%files -n mythes-nn
%doc README_th_nb_NO_v2.txt
%{_datadir}/mythes/th_nn_NO_v2.*
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.2-2
- Prepare for Oreon 11 (RP1)
