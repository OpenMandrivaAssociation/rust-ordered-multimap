%bcond_without check
%define debug_package %{nil}
%global crate ordered-multimap

Name:           rust-%{crate}
Version:        0.4.2
Release:        1
Summary:        Insertion ordered multimap

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/ordered-multimap
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging
%if ! %{__cargo_skip_build}
BuildRequires:  (crate(dlv-list/default) >= 0.3.0 with crate(dlv-list/default) < 0.4.0)
BuildRequires:  (crate(hashbrown/default) >= 0.11.0 with crate(hashbrown/default) < 0.12.0)
%endif

%global _description %{expand:
Insertion ordered multimap.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(ordered-multimap) = 0.4.2
Requires:       cargo
Requires:       (crate(dlv-list/default) >= 0.3.0 with crate(dlv-list/default) < 0.4.0)
Requires:       (crate(hashbrown/default) >= 0.11.0 with crate(hashbrown/default) < 0.12.0)

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc RELEASES.md README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(ordered-multimap/default) = 0.4.2
Requires:       cargo
Requires:       crate(ordered-multimap) = 0.4.2

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(ordered-multimap/serde) = 0.4.2
Requires:       cargo
Requires:       (crate(serde/default) >= 1.0.0 with crate(serde/default) < 2.0.0)
Requires:       crate(ordered-multimap) = 0.4.2

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
