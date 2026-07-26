%global source0_hash b8127fb6fe5562dfabfcb7d62df4ba2f018de39d7fbe7df2b7a688578516b4b7

%global docdir %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}

Name:		QuantLib
Version:	1.29
Release:	9%{?dist}
Summary:	A software framework for quantitative finance
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		http://www.quantlib.org
Source0:	https://dl.bintray.com/quantlib/releases/QuantLib-%{version}.tar.gz
BuildRequires: make
BuildRequires:  gcc, gcc-c++
BuildRequires:	boost-devel >= 1.43, texlive-latex, texlive-dvips, emacs

%description
QuantLib is a free/open-source library for modeling, trading, and 
risk management in real-life.

%package devel
Summary:	QuantLib development files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Static libraries and headers for QuantLib.

%package test
Summary:	The test-suite to check the setup of QuantLib
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description test
The QuantLib-test-suite will validate the compiled code against 
pre-constructed test cases, and helps in validating the library.

%package doc
Summary:	The documentation for QuantLib
Requires:	%{name} = %{version}
BuildRequires:	doxygen >= 1.3, graphviz

%description doc
This package contains documentation files generated from the source code of
QuantLib.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure --enable-intraday CFLAGS="$RPM_OPT_FLAGS -fpermissive" CPPFLAGS="$RPM_OPT_FLAGS -fpermissive"
# Get rid of RPATH
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
# pdf and ps file creation process breaks tetex
# make pdf-local ps-local

%install
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{docdir}
#cp -p Docs/latex/refman.pdf %{buildroot}%{docdir}/QuantLib-%{version}-docs-refman.pdf
#cp -p Docs/latex/refman.ps %{buildroot}%{docdir}/QuantLib-%{version}-docs-refman.ps
mkdir -p %{buildroot}%{_mandir}/man1/
cp -p man/*.1 %{buildroot}%{_mandir}/man1/
rm -rf %{buildroot}/%{_libdir}/*.la
rm -rf %{buildroot}/%{_libdir}/*.a
# So many of the names in the Quantlib manpages are generic, so we rename them to avoid conflicts.
%if 0
for i in history format gamma manips engines rate floor group license todo error deprecated attachment description domain.hpp method next value end y0 Constraint length; do
	if [ -f %{buildroot}%{_mandir}/man3/$i.3 ]; then
		mv %{buildroot}%{_mandir}/man3/$i.3 %{buildroot}%{_mandir}/man3/ql-$i.3
	else
		echo "$i.3 not found in %{buildroot}%{_mandir}/man3/"
	fi
done

# Get rid of spaces in man page names
mv "%{buildroot}%{_mandir}/man3/Singleton_ ExchangeRateManager _.3" %{buildroot}/%{_mandir}/man3/Singleton_ExchangeRateManager.3
# mv "%%{buildroot}%%{_mandir}/man3/Singleton_ IndexManager _.3" %%{buildroot}/%%{_mandir}/man3/Singleton_IndexManager.3
mv "%{buildroot}%{_mandir}/man3/operator Leg.3" %{buildroot}/%{_mandir}/man3/operator_Leg.3
mv "%{buildroot}%{_mandir}/man3/Singleton_ CommoditySettings _.3" %{buildroot}/%{_mandir}/man3/Singleton_CommoditySettings.3
mv "%{buildroot}%{_mandir}/man3/Singleton_ UnitOfMeasureConversionManager _.3" %{buildroot}/%{_mandir}/man3/Singleton_UnitOfMeasureConversionManager.3
# Fix file encoding
recode()
{
        iconv -f "$2" -t utf-8 < "$1" > "${1}_"
        mv -f "${1}_" "$1"
}
recode %{buildroot}%{_mandir}/man3/QuantLib_DKKCurrency.3 iso-8859-1
recode %{buildroot}%{_mandir}/man3/QuantLib_SEKCurrency.3 iso-8859-1
recode %{buildroot}%{_mandir}/man3/QuantLib_NOKCurrency.3 iso-8859-1
recode %{buildroot}%{_mandir}/man3/QuantLib_FIMCurrency.3 iso-8859-1
recode %{buildroot}%{_mandir}/man3/QuantLib_Currency.3 iso-8859-1
recode %{buildroot}%{_mandir}/man3/ql-group.3 iso-8859-1
recode %{buildroot}%{_mandir}/man3/ql-history.3 iso-8859-1
recode %{buildroot}%{_mandir}/man3/ql-license.3 iso-8859-1
%endif

# Fix multilib conflicts
touch -r News.md %{buildroot}%{_bindir}/quantlib-config
touch -r News.md %{buildroot}%{_datadir}/emacs/site-lisp/quantlib.elc

%ldconfig_scriptlets

%files
%doc LICENSE.TXT
%{_libdir}/libQuantLib.so.*

%files devel
%{_includedir}/ql/
%{_libdir}/libQuantLib.so
%{_libdir}/pkgconfig/quantlib.pc
%{_bindir}/quantlib-config
%{_mandir}/man1/quantlib-config.*
%{_mandir}/man1/quantlib-benchmark.*
%{_datadir}/aclocal/quantlib.m4
%{_datadir}/emacs/site-lisp/*

%files test
%{_bindir}/quantlib-test-suite
%{_mandir}/man1/quantlib-test-suite.*

%files doc
%doc Contributors.txt ChangeLog.txt README.md News.md
%if 0
%{_mandir}/man3/*
%endif
%{_mandir}/man1/BasketLosses.*
%{_mandir}/man1/Bonds.*
%{_mandir}/man1/BermudanSwaption.*
%{_mandir}/man1/CallableBonds.*
%{_mandir}/man1/CDS.*
%{_mandir}/man1/ConvertibleBonds.*
%{_mandir}/man1/CVAIRS.*
%{_mandir}/man1/DiscreteHedging.*
%{_mandir}/man1/EquityOption.*
%{_mandir}/man1/FittedBondCurve.*
%{_mandir}/man1/FRA.*
%{_mandir}/man1/Gaussian1dModels.*
%{_mandir}/man1/GlobalOptimizer.*
%{_mandir}/man1/LatentModel.*
%{_mandir}/man1/MarketModels.*
%{_mandir}/man1/MulticurveBootstrapping.*
%{_mandir}/man1/MultidimIntegral.*
%{_mandir}/man1/Replication.*
%{_mandir}/man1/Repo.*
#%%{docdir}/QuantLib-%%{version}-docs-refman.pdf
#%%{docdir}/QuantLib-%%{version}-docs-refman.ps

%changelog
%autochangelog
