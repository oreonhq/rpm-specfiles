%global source0_hash d239cc2310401903f6b79d458c2bbef5bf74c46f3f974ae9c1061fb74a404862
%global gem_name hashery
Name: rubygem-%{gem_name}
Version: 2.1.2
Release:        22%{?dist}
Summary:        Facets-bread collection of Hash-like classes
License: LicenseRef-Callaway-BSD
URL: http://rubyworks.github.com/hashery
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
The Hashery is a tight collection of Hash-like classes. Included among its
many offerings are the auto-sorting Dictionary class, the efficient LRUHash,
the flexible OpenHash and the convenient KeyHash. Nearly every class is a
subclass of the CRUDHash which defines a CRUD model on top of Ruby's standard
Hash making it a snap to subclass and augment to fit any specific use case.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -T
%gem_install -n %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-hashery-doc -f %{oreon_filedir}/rubygem-hashery-doc.list

%changelog

%autochangelog
