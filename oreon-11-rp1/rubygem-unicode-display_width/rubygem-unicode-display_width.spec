%global source0_hash 0cdd96b5681a5949cdbc2c55e7b420facae74c4aaf9a9815eee1087cb1853c42

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name unicode-display_width

Summary: Ruby library to determine the monospace display width of a string
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 3.2.0
Release: 1%{dist}
License: MIT
URL: https://github.com/janlelis/unicode-display_width
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems
BuildArch: noarch

%description
This gem provides an API to get the monospace display width of a string,
accounting for the rendered size of East Asian characters and other Unicode
classes, (optionally) including emoji.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}
%setup -n %{gem_name}-%{version} -T -D -q
%{?scl:scl enable %{scl} "}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:"}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}

%{?scl:scl enable %{scl} "}
%gem_install
%{?scl:"}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
if [ -e %{buildroot}%{gem_instdir}/.yardoc ]; then
	rm -f %{buildroot}%{gem_instdir}/.yardoc
fi

%files
%dir %{gem_instdir}
%{gem_libdir}
%license %{gem_instdir}/MIT-LICENSE.txt
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/data
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
%autochangelog
