%global source0_hash 4e463a634ef0ae48096886b4fe3a882eb24635c2a51dbe4154bdc54a0e2e5cba

Name:           R-arules
Version:        %R_rpm_version 1.7.13
Release:        %autorelease
Summary:        Mining Association Rules and Frequent Itemsets

License:        GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Provides the infrastructure for representing, manipulating and analyzing 
transaction data and patterns (frequent itemsets and association rules). 
Also provides C implementations of the association mining algorithms 
Apriori and Eclat. Hahsler, Gruen and Hornik (2005) 
<doi:10.18637/jss.v014.i15>.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-examples

%files -f %{R_files}

%changelog
%autochangelog
