%global source0_hash bfb042acdb481b3dc3165b5dd105a57679d912c5225ebd7c77b6b0e184b8cbfa

Name:			textcat
Version:		1.10
Release:		24%{?dist}
Summary:		Written language identification
%{?el5:Group:		Applications/Text}

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:		LicenseRef-Callaway-LGPLv2+
URL:			http://www.let.rug.nl/~vannoord/TextCat/
Source0:		%{url}text_cat.tgz
Source1:		%{url}%{name}.pdf

BuildRequires:		perl-interpreter
BuildRequires:		perl-generators
BuildRequires:		perl(Benchmark)
BuildRequires:		perl(Getopt::Std)
BuildRequires:		perl(strict)
BuildRequires:		perl(vars)

BuildArch:		noarch
%{?el5:BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)}

%description
TextCat is an implementation of the text categorization algorithm
presented in Cavnar, W. B. and J. M. Trenkle, "N-Gram-Based Text
Categorization".  TextCat uses this the technique to implement a
written language identification.  At the moment, it knows about 69
natural languages (counting Esperanto as a natural language).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qc
cp -a %{SOURCE1} .

%build
sed	-e '1{/^#!.*/d}' < text_cat > %{name}
sed -i	-e '1s~^~#!%{__perl} -w\n~'						\
	-e 's!/users1/vannoord/Perl/TextCat/LM!%{_datadir}/%{name}/lm!g'	\
	%{name}
touch	-r text_cat %{name}

%install
%{?el5:rm -rf %{buildroot}}
mkdir	-p %{buildroot}%{_bindir} %{buildroot}%{_datadir}/%{name}/lm
install -pm0755 %{name} %{buildroot}%{_bindir}
install -pm0644 LM/* %{buildroot}%{_datadir}/%{name}/lm

%check
sed	-e 's!%{_datadir}/%{name}/lm!%{buildroot}&!g'				\
	< %{name} > %{name}_test
for _test in `find ShortTexts/ -name '*.txt' | sort -u`
do
  %{__perl} -w %{name}_test ${_test}
done

%files
%doc CHANGES COPYING Copyright README %{name}.pdf
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
%autochangelog
