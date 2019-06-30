import matplotlib.pyplot as plt


class PalletExtractor():
    @staticmethod
    def plot_pallet(colors, iteration, radius=0.05, margin=0.15):
        base = 0.1
        fig, ax = plt.subplots()
        ax.set_axis_off()
        for c, i in zip(colors, range(len(colors))):
            circle = plt.Circle((0.3, base), radius, color=c)
            base += margin
            ax.add_artist(circle)
            ax.text(0.42, 0.22 + margin * (i - 1), str(c), fontsize=15, name="open sans")
        ax.text(0.3, 0.22 + (len(colors) - 1) * margin, 'Iteração {}'.format(iteration), fontsize=22, name='open sans')
        plt.savefig('../pallet_images/img_it{}.png'.format(iteration), transparent=True)
