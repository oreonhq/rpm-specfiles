%global source0_hash 390919de89822ad6d3ba3daf694d720be9d83ed95cdf7adf54d4573c98b17421

%global gem_name sys-filesystem

Name:           rubygem-%{gem_name}
Version:        1.4.3
Release:        %autorelease
Summary:        Interface for gathering filesystem information

License:        Apache-2.0
URL:            https://rubygems.org/gems/sys-filesystem
Source:         https://rubygems.org/downloads/%{gem_name}-%{version}.gem

BuildRequires:  rubygems-devel

BuildArch:      noarch

%description
%{summary}.

%package doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

rm -vr %{buildroot}%{gem_instdir}/{certs,spec}
rm -v %{buildroot}%{gem_cache}

%files
%license %{gem_instdir}/LICENSE
%dir %{gem_instdir}

%{gem_libdir}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/{{README,CHANGES,MANIFEST}.md,examples}
%{gem_instdir}/{Gemfile,Rakefile,%{gem_name}.gemspec}

%changelog
%autochangelog
