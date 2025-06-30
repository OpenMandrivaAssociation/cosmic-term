%undefine _debugsource_packages

%define         appname com.system76.CosmicTerm
Name:           cosmic-term
Version:        1.0.0
%define beta alpha.7
Release:        %{?beta:0.%{beta}.}1
Summary:        COSMIC terminal emulator
Group:          Terminal/COSMIC
License:        GPL-3.0-only
URL:            https://github.com/pop-os/cosmic-term
Source0:        https://github.com/pop-os/cosmic-term/archive/epoch-%{version}%{?beta:-%{beta}}/%{name}-epoch-%{version}%{?beta:-%{beta}}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config

BuildRequires:  rust-packaging
BuildRequires:  git-core
BuildRequires:  hicolor-icon-theme
BuildRequires:  just
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xkbcommon)
#Requires:       mozilla-fira-fonts
#Recommends:     google-noto-coloremoji-fonts

%description
COSMIC terminal emulator, built using alacritty_terminal that is provided by the
alacritty project. cosmic-term provides bidirectional rendering and ligatures
with a custom renderer based on cosmic-text.

%prep
%autosetup -n %{name}-epoch-%{version}%{?beta:-%{beta}} -a1 -p1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
# Build failure workaround: https://github.com/pop-os/cosmic-files/issues/392#issuecomment-2308954953
export VERGEN_GIT_COMMIT_DATE="$(date --utc '+%Y-%m-%d %H:%M:%S %z')"
export VERGEN_GIT_SHA=$_commit
just build-release

%install
just rootdir=%{buildroot} prefix=%{_prefix} install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/icons/hicolor/??x??/apps/%{appname}.svg
%{_datadir}/icons/hicolor/???x???/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.metainfo.xml
