%global	gem_name	rspec

Summary:	Behaviour driven development (BDD) framework for Ruby
Name:		rubygem-%{gem_name}
Version:	3.13.2
Release:	2%{?dist}

License:	MIT
URL:		http://rspec.info
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
# oreon url source checksums begin
%global source0_sha256 206284a08ad798e61f86d7ca3e376718d52c0bc944626b2349266f239f820587
%global source0_file rspec-3.13.2.gem
# oreon url source checksums end

BuildRequires:	rubygems-devel
#BuildRequires:	ruby(release)

BuildArch:	noarch

%description
RSpec is a behaviour driven development (BDD) framework for Ruby.  

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}

%description	doc
This package contains documentation for %{name}.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/rspec-3.13.2.gem; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "206284a08ad798e61f86d7ca3e376718d52c0bc944626b2349266f239f820587" || { echo "oreon: Source0 SHA256 mismatch for rspec-3.13.2.gem" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

%build
gem build %{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

rm -f %{buildroot}%{gem_cache}

%files
%dir	%{gem_instdir}
%{gem_instdir}/lib
%license	%{gem_instdir}/LICENSE.md
%doc	%{gem_instdir}/README.md
%{gem_spec}

%files	doc
%doc	%{gem_docdir}


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.13.2-2
- Prepare for Oreon 11 (RP1)
